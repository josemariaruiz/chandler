/////////////////////////////////////////////////////////////////////////////
// Name:        common/fontcmn.cpp
// Purpose:     implementation of wxFontBase methods
// Author:      Vadim Zeitlin
// Modified by:
// Created:     20.09.99
// RCS-ID:      $Id$
// Copyright:   (c) wxWidgets team
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

// ============================================================================
// declarations
// ============================================================================

// ----------------------------------------------------------------------------
// headers
// ----------------------------------------------------------------------------

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
#pragma implementation "fontbase.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
#pragma hdrstop
#endif

#ifndef WX_PRECOMP
    #include "wx/dc.h"
    #include "wx/font.h"
    #include "wx/intl.h"
    #include "wx/dcscreen.h"
#endif // WX_PRECOMP

#include "wx/gdicmn.h"

#if defined(__WXMSW__)
  #include  "wx/msw/private.h"  // includes windows.h for LOGFONT
  #include  "wx/msw/winundef.h"
#endif

#include "wx/fontutil.h" // for wxNativeFontInfo
#include "wx/fontmap.h"

#include "wx/tokenzr.h"

// ============================================================================
// implementation
// ============================================================================

// ----------------------------------------------------------------------------
// helper functions
// ----------------------------------------------------------------------------

static void AdjustFontSize(wxFont& font, wxDC& dc, const wxSize& pixelSize)
{
    int currentSize = font.GetPointSize();
    int largestGood = 0;
    int smallestBad = 0;

    bool initialGoodFound = false;
    bool initialBadFound = false;

    while (currentSize > 0)
    {
        dc.SetFont(font);

        // if currentSize (in points) results in a font that is smaller
        // than required by pixelSize it is considered a good size
        if (dc.GetCharHeight() <= pixelSize.GetHeight() &&
                (!pixelSize.GetWidth() ||
                 dc.GetCharWidth() <= pixelSize.GetWidth()))
        {
            largestGood = currentSize;
            initialGoodFound = true;
        }
        else
        {
            smallestBad = currentSize;
            initialBadFound = true;
        }
        if (!initialGoodFound)
        {
            currentSize /= 2;
        }
        else if (!initialBadFound)
        {
            currentSize *= 2;
        }
        else
        {
            int distance = smallestBad - largestGood;
            if (distance == 1)
                break;

            currentSize = largestGood + distance / 2;
        }

        font.SetPointSize(currentSize);
    }

    if (currentSize != largestGood)
        font.SetPointSize(largestGood);
}

// ----------------------------------------------------------------------------
// wxFontBase
// ----------------------------------------------------------------------------

wxFontEncoding wxFontBase::ms_encodingDefault = wxFONTENCODING_SYSTEM;

/* static */
void wxFontBase::SetDefaultEncoding(wxFontEncoding encoding)
{
    // GetDefaultEncoding() should return something != wxFONTENCODING_DEFAULT
    // and, besides, using this value here doesn't make any sense
    wxCHECK_RET( encoding != wxFONTENCODING_DEFAULT,
                 _T("can't set default encoding to wxFONTENCODING_DEFAULT") );

    ms_encodingDefault = encoding;
}

wxFontBase::~wxFontBase()
{
    // this destructor is required for Darwin
}

/* static */
wxFont *wxFontBase::New(int size,
                        int family,
                        int style,
                        int weight,
                        bool underlined,
                        const wxString& face,
                        wxFontEncoding encoding)
{
    return new wxFont(size, family, style, weight, underlined, face, encoding);
}

static inline int flags2Style(int flags)
{
    return flags & wxFONTFLAG_ITALIC
                    ? wxFONTSTYLE_ITALIC
                    : flags & wxFONTFLAG_SLANT
                        ? wxFONTSTYLE_SLANT
                        : wxFONTSTYLE_NORMAL;
}

static inline int flags2Weight(int flags)
{
    return flags & wxFONTFLAG_LIGHT
                    ? wxFONTWEIGHT_LIGHT
                    : flags & wxFONTFLAG_BOLD
                        ? wxFONTWEIGHT_BOLD
                        : wxFONTWEIGHT_NORMAL;
}

static inline bool flags2Underlined(int flags)
{
    return (flags & wxFONTFLAG_UNDERLINED) != 0;
}

/* static */
wxFont *wxFontBase::New(int pointSize,
                        wxFontFamily family,
                        int flags,
                        const wxString& face,
                        wxFontEncoding encoding)
{
    return New(pointSize, family, flags2Style(flags), flags2Weight(flags),
               flags2Underlined(flags), face, encoding);
}

/* static */
wxFont *wxFontBase::New(const wxSize& pixelSize,
                        int family,
                        int style,
                        int weight,
                        bool underlined,
                        const wxString& face,
                        wxFontEncoding encoding)
{
#if defined(__WXMSW__)
    return new wxFont(pixelSize, family, style, weight, underlined,
                      face, encoding);
#else
    wxFont *self = New(10, family, style, weight, underlined, face, encoding);
    wxScreenDC dc;
    AdjustFontSize(*(wxFont *)self, dc, pixelSize);
    return self;
#endif
}

/* static */
wxFont *wxFontBase::New(const wxSize& pixelSize,
                        wxFontFamily family,
                        int flags,
                        const wxString& face,
                        wxFontEncoding encoding)
{
    return New(pixelSize, family, flags2Style(flags), flags2Weight(flags),
               flags2Underlined(flags), face, encoding);
}

wxSize wxFontBase::GetPixelSize() const
{
    wxScreenDC dc;
    dc.SetFont(*(wxFont *)this);
    return wxSize(dc.GetCharWidth(), dc.GetCharHeight());
}

bool wxFontBase::IsUsingSizeInPixels() const
{
    return false;
}

void wxFontBase::SetPixelSize( const wxSize& pixelSize )
{
    wxScreenDC dc;
    AdjustFontSize(*(wxFont *)this, dc, pixelSize);
}

/* static */
wxFont *wxFontBase::New(const wxNativeFontInfo& info)
{
    return new wxFont(info);
}

/* static */
wxFont *wxFontBase::New(const wxString& strNativeFontDesc)
{
    wxNativeFontInfo fontInfo;
    if ( !fontInfo.FromString(strNativeFontDesc) )
        return new wxFont(*wxNORMAL_FONT);

    return New(fontInfo);
}

bool wxFontBase::IsFixedWidth() const
{
    return GetFamily() == wxFONTFAMILY_TELETYPE;
}

void wxFontBase::DoSetNativeFontInfo(const wxNativeFontInfo& info)
{
#ifdef wxNO_NATIVE_FONTINFO
    SetPointSize(info.pointSize);
    SetFamily(info.family);
    SetStyle(info.style);
    SetWeight(info.weight);
    SetUnderlined(info.underlined);
    SetFaceName(info.faceName);
    SetEncoding(info.encoding);
#else
    (void)info;
#endif
}

wxString wxFontBase::GetNativeFontInfoDesc() const
{
    wxString fontDesc;
    const wxNativeFontInfo *fontInfo = GetNativeFontInfo();
    if ( fontInfo )
    {
        fontDesc = fontInfo->ToString();
    }

    return fontDesc;
}

wxString wxFontBase::GetNativeFontInfoUserDesc() const
{
    wxString fontDesc;
    const wxNativeFontInfo *fontInfo = GetNativeFontInfo();
    if ( fontInfo )
    {
        fontDesc = fontInfo->ToUserString();
    }

    return fontDesc;
}

void wxFontBase::SetNativeFontInfo(const wxString& info)
{
    wxNativeFontInfo fontInfo;
    if ( !info.empty() && fontInfo.FromString(info) )
    {
        SetNativeFontInfo(fontInfo);
    }
}

void wxFontBase::SetNativeFontInfoUserDesc(const wxString& info)
{
    wxNativeFontInfo fontInfo;
    if ( !info.empty() && fontInfo.FromUserString(info) )
    {
        SetNativeFontInfo(fontInfo);
    }
}

wxFont& wxFont::operator=(const wxFont& font)
{
    if ( this != &font )
        Ref(font);

    return (wxFont &)*this;
}

bool wxFontBase::operator==(const wxFont& font) const
{
    // either it is the same font, i.e. they share the same common data or they
    // have different ref datas but still describe the same font
    return GetFontData() == font.GetFontData() ||
           (
            Ok() == font.Ok() &&
            GetPointSize() == font.GetPointSize() &&
            GetFamily() == font.GetFamily() &&
            GetStyle() == font.GetStyle() &&
            GetWeight() == font.GetWeight() &&
            GetUnderlined() == font.GetUnderlined() &&
            GetFaceName() == font.GetFaceName() &&
            GetEncoding() == font.GetEncoding()
           );
}

bool wxFontBase::operator!=(const wxFont& font) const
{
    return !(*this == font);
}

wxString wxFontBase::GetFamilyString() const
{
    wxCHECK_MSG( Ok(), wxT("wxDEFAULT"), wxT("invalid font") );

    switch ( GetFamily() )
    {
        case wxDECORATIVE:   return wxT("wxDECORATIVE");
        case wxROMAN:        return wxT("wxROMAN");
        case wxSCRIPT:       return wxT("wxSCRIPT");
        case wxSWISS:        return wxT("wxSWISS");
        case wxMODERN:       return wxT("wxMODERN");
        case wxTELETYPE:     return wxT("wxTELETYPE");
        default:             return wxT("wxDEFAULT");
    }
}

wxString wxFontBase::GetStyleString() const
{
    wxCHECK_MSG( Ok(), wxT("wxDEFAULT"), wxT("invalid font") );

    switch ( GetStyle() )
    {
        case wxNORMAL:   return wxT("wxNORMAL");
        case wxSLANT:    return wxT("wxSLANT");
        case wxITALIC:   return wxT("wxITALIC");
        default:         return wxT("wxDEFAULT");
    }
}

wxString wxFontBase::GetWeightString() const
{
    wxCHECK_MSG( Ok(), wxT("wxDEFAULT"), wxT("invalid font") );

    switch ( GetWeight() )
    {
        case wxNORMAL:   return wxT("wxNORMAL");
        case wxBOLD:     return wxT("wxBOLD");
        case wxLIGHT:    return wxT("wxLIGHT");
        default:         return wxT("wxDEFAULT");
    }
}

// ----------------------------------------------------------------------------
// wxNativeFontInfo
// ----------------------------------------------------------------------------

#ifdef wxNO_NATIVE_FONTINFO

// These are the generic forms of FromString()/ToString.
//
// convert to/from the string representation: format is
//      version;pointsize;family;style;weight;underlined;facename;encoding

bool wxNativeFontInfo::FromString(const wxString& s)
{
    long l;

    wxStringTokenizer tokenizer(s, _T(";"));

    wxString token = tokenizer.GetNextToken();
    //
    //  Ignore the version for now
    //

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    pointSize = (int)l;

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    family = (wxFontFamily)l;

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    style = (wxFontStyle)l;

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    weight = (wxFontWeight)l;

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    underlined = l != 0;

    faceName = tokenizer.GetNextToken();

#ifndef __WXMAC__
    if( !faceName )
        return false;
#endif

    token = tokenizer.GetNextToken();
    if ( !token.ToLong(&l) )
        return false;
    encoding = (wxFontEncoding)l;

    return true;
}

wxString wxNativeFontInfo::ToString() const
{
    wxString s;

    s.Printf(_T("%d;%d;%d;%d;%d;%d;%s;%d"),
             0,                                 // version
             pointSize,
             family,
             (int)style,
             (int)weight,
             underlined,
             faceName.GetData(),
             (int)encoding);

    return s;
}

void wxNativeFontInfo::Init()
{
    pointSize = 0;
    family = wxFONTFAMILY_DEFAULT;
    style = wxFONTSTYLE_NORMAL;
    weight = wxFONTWEIGHT_NORMAL;
    underlined = false;
    faceName.clear();
    encoding = wxFONTENCODING_DEFAULT;
}

int wxNativeFontInfo::GetPointSize() const
{
    return pointSize;
}

wxFontStyle wxNativeFontInfo::GetStyle() const
{
    return style;
}

wxFontWeight wxNativeFontInfo::GetWeight() const
{
    return weight;
}

bool wxNativeFontInfo::GetUnderlined() const
{
    return underlined;
}

wxString wxNativeFontInfo::GetFaceName() const
{
    return faceName;
}

wxFontFamily wxNativeFontInfo::GetFamily() const
{
    return family;
}

wxFontEncoding wxNativeFontInfo::GetEncoding() const
{
    return encoding;
}

void wxNativeFontInfo::SetPointSize(int pointsize)
{
    pointSize = pointsize;
}

void wxNativeFontInfo::SetStyle(wxFontStyle style_)
{
    style = style_;
}

void wxNativeFontInfo::SetWeight(wxFontWeight weight_)
{
    weight = weight_;
}

void wxNativeFontInfo::SetUnderlined(bool underlined_)
{
    underlined = underlined_;
}

void wxNativeFontInfo::SetFaceName(wxString facename_)
{
    faceName = facename_;
}

void wxNativeFontInfo::SetFamily(wxFontFamily family_)
{
    family = family_;
}

void wxNativeFontInfo::SetEncoding(wxFontEncoding encoding_)
{
    encoding = encoding_;
}

#endif // generic wxNativeFontInfo implementation

// conversion to/from user-readable string: this is used in the generic
// versions and under MSW as well because there is no standard font description
// format there anyhow (but there is a well-defined standard for X11 fonts used
// by wxGTK and wxMotif)

#if defined(wxNO_NATIVE_FONTINFO) || defined(__WXMSW__) || defined (__WXPM__)

wxString wxNativeFontInfo::ToUserString() const
{
    wxString desc;

    // first put the adjectives, if any - this is English-centric, of course,
    // but what else can we do?
    if ( GetUnderlined() )
    {
        desc << _("underlined ");
    }

    switch ( GetWeight() )
    {
        default:
            wxFAIL_MSG( _T("unknown font weight") );
            // fall through

        case wxFONTWEIGHT_NORMAL:
            break;

        case wxFONTWEIGHT_LIGHT:
            desc << _("light ");
            break;

        case wxFONTWEIGHT_BOLD:
            desc << _("bold ");
            break;
    }

    switch ( GetStyle() )
    {
        default:
            wxFAIL_MSG( _T("unknown font style") );
            // fall through

        case wxFONTSTYLE_NORMAL:
            break;

            // we don't distinguish between the two for now anyhow...
        case wxFONTSTYLE_ITALIC:
        case wxFONTSTYLE_SLANT:
            desc << _("italic");
            break;
    }

    wxString face = GetFaceName();
    if ( !face.empty() )
    {
        desc << _T(' ') << face;
    }

    int size = GetPointSize();
    if ( size != wxNORMAL_FONT->GetPointSize() )
    {
        desc << _T(' ') << size;
    }

#if wxUSE_FONTMAP
    wxFontEncoding enc = GetEncoding();
    if ( enc != wxFONTENCODING_DEFAULT && enc != wxFONTENCODING_SYSTEM )
    {
        desc << _T(' ') << wxFontMapper::GetEncodingName(enc);
    }
#endif // wxUSE_FONTMAP

    return desc;
}

bool wxNativeFontInfo::FromUserString(const wxString& s)
{
    // reset to the default state
    Init();

    // parse a more or less free form string
    //
    // TODO: we should handle at least the quoted facenames
    wxStringTokenizer tokenizer(s, _T(";, "), wxTOKEN_STRTOK);

    wxString face;
    unsigned long size;

#if wxUSE_FONTMAP
    wxFontEncoding encoding;
#endif // wxUSE_FONTMAP

    while ( tokenizer.HasMoreTokens() )
    {
        wxString token = tokenizer.GetNextToken();

        // normalize it
        token.Trim(true).Trim(false).MakeLower();

        // look for the known tokens
        if ( token == _T("underlined") || token == _("underlined") )
        {
            SetUnderlined(true);
        }
        else if ( token == _T("light") || token == _("light") )
        {
            SetWeight(wxFONTWEIGHT_LIGHT);
        }
        else if ( token == _T("bold") || token == _("bold") )
        {
            SetWeight(wxFONTWEIGHT_BOLD);
        }
        else if ( token == _T("italic") || token == _("italic") )
        {
            SetStyle(wxFONTSTYLE_ITALIC);
        }
        else if ( token.ToULong(&size) )
        {
            SetPointSize(size);
        }
#if wxUSE_FONTMAP
        else if ( (encoding = wxFontMapper::Get()->CharsetToEncoding(token, false))
                    != wxFONTENCODING_DEFAULT )
        {
            SetEncoding(encoding);
        }
#endif // wxUSE_FONTMAP
        else // assume it is the face name
        {
            if ( !face.empty() )
            {
                face += _T(' ');
            }

            face += token;

            // skip the code which resets face below
            continue;
        }

        // if we had had the facename, we shouldn't continue appending tokens
        // to it (i.e. "foo bold bar" shouldn't result in the facename "foo
        // bar")
        if ( !face.empty() )
        {
            SetFaceName(face);
            face.clear();
        }
    }

    // we might not have flushed it inside the loop
    if ( !face.empty() )
    {
        SetFaceName(face);
    }

    return true;
}

#endif // generic or wxMSW or wxOS2

