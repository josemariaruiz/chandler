## This file reverse renames symbols in the wx package to give
## them their wx prefix again, for backwards compatibility.
##
## Generated by BuildRenamers in config.py

# This silly stuff here is so the wxPython.wx module doesn't conflict
# with the wx package.  We need to import modules from the wx package
# here, then we'll put the wxPython.wx entry back in sys.modules.
import sys
_wx = None
if sys.modules.has_key('wxPython.wx'):
    _wx = sys.modules['wxPython.wx']
    del sys.modules['wxPython.wx']

import wx._windows

sys.modules['wxPython.wx'] = _wx
del sys, _wx


# Now assign all the reverse-renamed names:
wxPanel = wx._windows.Panel
wxPanelPtr = wx._windows.PanelPtr
wxPrePanel = wx._windows.PrePanel
wxPanel_GetClassDefaultAttributes = wx._windows.Panel_GetClassDefaultAttributes
wxScrolledWindow = wx._windows.ScrolledWindow
wxScrolledWindowPtr = wx._windows.ScrolledWindowPtr
wxPreScrolledWindow = wx._windows.PreScrolledWindow
wxScrolledWindow_GetClassDefaultAttributes = wx._windows.ScrolledWindow_GetClassDefaultAttributes
wxFrameNameStr = wx._windows.FrameNameStr
wxDialogNameStr = wx._windows.DialogNameStr
wxStatusLineNameStr = wx._windows.StatusLineNameStr
wxToolBarNameStr = wx._windows.ToolBarNameStr
wxSTAY_ON_TOP = wx._windows.STAY_ON_TOP
wxICONIZE = wx._windows.ICONIZE
wxMINIMIZE = wx._windows.MINIMIZE
wxMAXIMIZE = wx._windows.MAXIMIZE
wxCLOSE_BOX = wx._windows.CLOSE_BOX
wxTHICK_FRAME = wx._windows.THICK_FRAME
wxSYSTEM_MENU = wx._windows.SYSTEM_MENU
wxMINIMIZE_BOX = wx._windows.MINIMIZE_BOX
wxMAXIMIZE_BOX = wx._windows.MAXIMIZE_BOX
wxTINY_CAPTION_HORIZ = wx._windows.TINY_CAPTION_HORIZ
wxTINY_CAPTION_VERT = wx._windows.TINY_CAPTION_VERT
wxRESIZE_BOX = wx._windows.RESIZE_BOX
wxRESIZE_BORDER = wx._windows.RESIZE_BORDER
wxDIALOG_NO_PARENT = wx._windows.DIALOG_NO_PARENT
wxDEFAULT_FRAME_STYLE = wx._windows.DEFAULT_FRAME_STYLE
wxDEFAULT_DIALOG_STYLE = wx._windows.DEFAULT_DIALOG_STYLE
wxFRAME_TOOL_WINDOW = wx._windows.FRAME_TOOL_WINDOW
wxFRAME_FLOAT_ON_PARENT = wx._windows.FRAME_FLOAT_ON_PARENT
wxFRAME_NO_WINDOW_MENU = wx._windows.FRAME_NO_WINDOW_MENU
wxFRAME_NO_TASKBAR = wx._windows.FRAME_NO_TASKBAR
wxFRAME_SHAPED = wx._windows.FRAME_SHAPED
wxDIALOG_MODAL = wx._windows.DIALOG_MODAL
wxDIALOG_MODELESS = wx._windows.DIALOG_MODELESS
wxUSER_COLOURS = wx._windows.USER_COLOURS
wxNO_3D = wx._windows.NO_3D
wxFULLSCREEN_NOMENUBAR = wx._windows.FULLSCREEN_NOMENUBAR
wxFULLSCREEN_NOTOOLBAR = wx._windows.FULLSCREEN_NOTOOLBAR
wxFULLSCREEN_NOSTATUSBAR = wx._windows.FULLSCREEN_NOSTATUSBAR
wxFULLSCREEN_NOBORDER = wx._windows.FULLSCREEN_NOBORDER
wxFULLSCREEN_NOCAPTION = wx._windows.FULLSCREEN_NOCAPTION
wxFULLSCREEN_ALL = wx._windows.FULLSCREEN_ALL
wxTOPLEVEL_EX_DIALOG = wx._windows.TOPLEVEL_EX_DIALOG
wxUSER_ATTENTION_INFO = wx._windows.USER_ATTENTION_INFO
wxUSER_ATTENTION_ERROR = wx._windows.USER_ATTENTION_ERROR
wxTopLevelWindow = wx._windows.TopLevelWindow
wxTopLevelWindowPtr = wx._windows.TopLevelWindowPtr
wxFrame = wx._windows.Frame
wxFramePtr = wx._windows.FramePtr
wxPreFrame = wx._windows.PreFrame
wxFrame_GetClassDefaultAttributes = wx._windows.Frame_GetClassDefaultAttributes
wxDialog = wx._windows.Dialog
wxDialogPtr = wx._windows.DialogPtr
wxPreDialog = wx._windows.PreDialog
wxDialog_GetClassDefaultAttributes = wx._windows.Dialog_GetClassDefaultAttributes
wxMiniFrame = wx._windows.MiniFrame
wxMiniFramePtr = wx._windows.MiniFramePtr
wxPreMiniFrame = wx._windows.PreMiniFrame
wxSPLASH_CENTRE_ON_PARENT = wx._windows.SPLASH_CENTRE_ON_PARENT
wxSPLASH_CENTRE_ON_SCREEN = wx._windows.SPLASH_CENTRE_ON_SCREEN
wxSPLASH_NO_CENTRE = wx._windows.SPLASH_NO_CENTRE
wxSPLASH_TIMEOUT = wx._windows.SPLASH_TIMEOUT
wxSPLASH_NO_TIMEOUT = wx._windows.SPLASH_NO_TIMEOUT
wxSplashScreenWindow = wx._windows.SplashScreenWindow
wxSplashScreenWindowPtr = wx._windows.SplashScreenWindowPtr
wxSplashScreen = wx._windows.SplashScreen
wxSplashScreenPtr = wx._windows.SplashScreenPtr
wxSB_NORMAL = wx._windows.SB_NORMAL
wxSB_FLAT = wx._windows.SB_FLAT
wxSB_RAISED = wx._windows.SB_RAISED
wxStatusBar = wx._windows.StatusBar
wxStatusBarPtr = wx._windows.StatusBarPtr
wxPreStatusBar = wx._windows.PreStatusBar
wxStatusBar_GetClassDefaultAttributes = wx._windows.StatusBar_GetClassDefaultAttributes
wxSplitterNameStr = wx._windows.SplitterNameStr
wxSP_NOBORDER = wx._windows.SP_NOBORDER
wxSP_NOSASH = wx._windows.SP_NOSASH
wxSP_PERMIT_UNSPLIT = wx._windows.SP_PERMIT_UNSPLIT
wxSP_LIVE_UPDATE = wx._windows.SP_LIVE_UPDATE
wxSP_3DSASH = wx._windows.SP_3DSASH
wxSP_3DBORDER = wx._windows.SP_3DBORDER
wxSP_NO_XP_THEME = wx._windows.SP_NO_XP_THEME
wxSP_BORDER = wx._windows.SP_BORDER
wxSP_3D = wx._windows.SP_3D
wxSPLIT_HORIZONTAL = wx._windows.SPLIT_HORIZONTAL
wxSPLIT_VERTICAL = wx._windows.SPLIT_VERTICAL
wxSPLIT_DRAG_NONE = wx._windows.SPLIT_DRAG_NONE
wxSPLIT_DRAG_DRAGGING = wx._windows.SPLIT_DRAG_DRAGGING
wxSPLIT_DRAG_LEFT_DOWN = wx._windows.SPLIT_DRAG_LEFT_DOWN
wxSplitterWindow = wx._windows.SplitterWindow
wxSplitterWindowPtr = wx._windows.SplitterWindowPtr
wxPreSplitterWindow = wx._windows.PreSplitterWindow
wxSplitterWindow_GetClassDefaultAttributes = wx._windows.SplitterWindow_GetClassDefaultAttributes
wxSplitterEvent = wx._windows.SplitterEvent
wxSplitterEventPtr = wx._windows.SplitterEventPtr
wxEVT_COMMAND_SPLITTER_SASH_POS_CHANGED = wx._windows.wxEVT_COMMAND_SPLITTER_SASH_POS_CHANGED
wxEVT_COMMAND_SPLITTER_SASH_POS_CHANGING = wx._windows.wxEVT_COMMAND_SPLITTER_SASH_POS_CHANGING
wxEVT_COMMAND_SPLITTER_DOUBLECLICKED = wx._windows.wxEVT_COMMAND_SPLITTER_DOUBLECLICKED
wxEVT_COMMAND_SPLITTER_UNSPLIT = wx._windows.wxEVT_COMMAND_SPLITTER_UNSPLIT
wxSashNameStr = wx._windows.SashNameStr
wxSashLayoutNameStr = wx._windows.SashLayoutNameStr
wxSASH_DRAG_NONE = wx._windows.SASH_DRAG_NONE
wxSASH_DRAG_DRAGGING = wx._windows.SASH_DRAG_DRAGGING
wxSASH_DRAG_LEFT_DOWN = wx._windows.SASH_DRAG_LEFT_DOWN
wxSW_NOBORDER = wx._windows.SW_NOBORDER
wxSW_BORDER = wx._windows.SW_BORDER
wxSW_3DSASH = wx._windows.SW_3DSASH
wxSW_3DBORDER = wx._windows.SW_3DBORDER
wxSW_3D = wx._windows.SW_3D
wxSASH_TOP = wx._windows.SASH_TOP
wxSASH_RIGHT = wx._windows.SASH_RIGHT
wxSASH_BOTTOM = wx._windows.SASH_BOTTOM
wxSASH_LEFT = wx._windows.SASH_LEFT
wxSASH_NONE = wx._windows.SASH_NONE
wxSashWindow = wx._windows.SashWindow
wxSashWindowPtr = wx._windows.SashWindowPtr
wxPreSashWindow = wx._windows.PreSashWindow
wxSASH_STATUS_OK = wx._windows.SASH_STATUS_OK
wxSASH_STATUS_OUT_OF_RANGE = wx._windows.SASH_STATUS_OUT_OF_RANGE
wxSashEvent = wx._windows.SashEvent
wxSashEventPtr = wx._windows.SashEventPtr
wxEVT_SASH_DRAGGED = wx._windows.wxEVT_SASH_DRAGGED
wxLAYOUT_HORIZONTAL = wx._windows.LAYOUT_HORIZONTAL
wxLAYOUT_VERTICAL = wx._windows.LAYOUT_VERTICAL
wxLAYOUT_NONE = wx._windows.LAYOUT_NONE
wxLAYOUT_TOP = wx._windows.LAYOUT_TOP
wxLAYOUT_LEFT = wx._windows.LAYOUT_LEFT
wxLAYOUT_RIGHT = wx._windows.LAYOUT_RIGHT
wxLAYOUT_BOTTOM = wx._windows.LAYOUT_BOTTOM
wxLAYOUT_LENGTH_Y = wx._windows.LAYOUT_LENGTH_Y
wxLAYOUT_LENGTH_X = wx._windows.LAYOUT_LENGTH_X
wxLAYOUT_MRU_LENGTH = wx._windows.LAYOUT_MRU_LENGTH
wxLAYOUT_QUERY = wx._windows.LAYOUT_QUERY
wxEVT_QUERY_LAYOUT_INFO = wx._windows.wxEVT_QUERY_LAYOUT_INFO
wxEVT_CALCULATE_LAYOUT = wx._windows.wxEVT_CALCULATE_LAYOUT
wxQueryLayoutInfoEvent = wx._windows.QueryLayoutInfoEvent
wxQueryLayoutInfoEventPtr = wx._windows.QueryLayoutInfoEventPtr
wxCalculateLayoutEvent = wx._windows.CalculateLayoutEvent
wxCalculateLayoutEventPtr = wx._windows.CalculateLayoutEventPtr
wxSashLayoutWindow = wx._windows.SashLayoutWindow
wxSashLayoutWindowPtr = wx._windows.SashLayoutWindowPtr
wxPreSashLayoutWindow = wx._windows.PreSashLayoutWindow
wxLayoutAlgorithm = wx._windows.LayoutAlgorithm
wxLayoutAlgorithmPtr = wx._windows.LayoutAlgorithmPtr
wxPopupWindow = wx._windows.PopupWindow
wxPopupWindowPtr = wx._windows.PopupWindowPtr
wxPrePopupWindow = wx._windows.PrePopupWindow
wxPopupTransientWindow = wx._windows.PopupTransientWindow
wxPopupTransientWindowPtr = wx._windows.PopupTransientWindowPtr
wxPrePopupTransientWindow = wx._windows.PrePopupTransientWindow
wxTipWindow = wx._windows.TipWindow
wxTipWindowPtr = wx._windows.TipWindowPtr
wxVScrolledWindow = wx._windows.VScrolledWindow
wxVScrolledWindowPtr = wx._windows.VScrolledWindowPtr
wxPreVScrolledWindow = wx._windows.PreVScrolledWindow
wxVListBoxNameStr = wx._windows.VListBoxNameStr
wxVListBox = wx._windows.VListBox
wxVListBoxPtr = wx._windows.VListBoxPtr
wxPreVListBox = wx._windows.PreVListBox
wxHtmlListBox = wx._windows.HtmlListBox
wxHtmlListBoxPtr = wx._windows.HtmlListBoxPtr
wxPreHtmlListBox = wx._windows.PreHtmlListBox
wxTaskBarIcon = wx._windows.TaskBarIcon
wxTaskBarIconPtr = wx._windows.TaskBarIconPtr
wxTaskBarIconEvent = wx._windows.TaskBarIconEvent
wxTaskBarIconEventPtr = wx._windows.TaskBarIconEventPtr
wxEVT_TASKBAR_MOVE = wx._windows.wxEVT_TASKBAR_MOVE
wxEVT_TASKBAR_LEFT_DOWN = wx._windows.wxEVT_TASKBAR_LEFT_DOWN
wxEVT_TASKBAR_LEFT_UP = wx._windows.wxEVT_TASKBAR_LEFT_UP
wxEVT_TASKBAR_RIGHT_DOWN = wx._windows.wxEVT_TASKBAR_RIGHT_DOWN
wxEVT_TASKBAR_RIGHT_UP = wx._windows.wxEVT_TASKBAR_RIGHT_UP
wxEVT_TASKBAR_LEFT_DCLICK = wx._windows.wxEVT_TASKBAR_LEFT_DCLICK
wxEVT_TASKBAR_RIGHT_DCLICK = wx._windows.wxEVT_TASKBAR_RIGHT_DCLICK
wxFileSelectorPromptStr = wx._windows.FileSelectorPromptStr
wxDirSelectorPromptStr = wx._windows.DirSelectorPromptStr
wxDirDialogNameStr = wx._windows.DirDialogNameStr
wxFileSelectorDefaultWildcardStr = wx._windows.FileSelectorDefaultWildcardStr
wxGetTextFromUserPromptStr = wx._windows.GetTextFromUserPromptStr
wxMessageBoxCaptionStr = wx._windows.MessageBoxCaptionStr
wxColourData = wx._windows.ColourData
wxColourDataPtr = wx._windows.ColourDataPtr
wxColourDialog = wx._windows.ColourDialog
wxColourDialogPtr = wx._windows.ColourDialogPtr
wxDirDialog = wx._windows.DirDialog
wxDirDialogPtr = wx._windows.DirDialogPtr
wxFileDialog = wx._windows.FileDialog
wxFileDialogPtr = wx._windows.FileDialogPtr
wxCHOICEDLG_STYLE = wx._windows.CHOICEDLG_STYLE
wxMultiChoiceDialog = wx._windows.MultiChoiceDialog
wxMultiChoiceDialogPtr = wx._windows.MultiChoiceDialogPtr
wxSingleChoiceDialog = wx._windows.SingleChoiceDialog
wxSingleChoiceDialogPtr = wx._windows.SingleChoiceDialogPtr
wxTextEntryDialog = wx._windows.TextEntryDialog
wxTextEntryDialogPtr = wx._windows.TextEntryDialogPtr
wxFontData = wx._windows.FontData
wxFontDataPtr = wx._windows.FontDataPtr
wxFontDialog = wx._windows.FontDialog
wxFontDialogPtr = wx._windows.FontDialogPtr
wxMessageDialog = wx._windows.MessageDialog
wxMessageDialogPtr = wx._windows.MessageDialogPtr
wxProgressDialog = wx._windows.ProgressDialog
wxProgressDialogPtr = wx._windows.ProgressDialogPtr
wxFR_DOWN = wx._windows.FR_DOWN
wxFR_WHOLEWORD = wx._windows.FR_WHOLEWORD
wxFR_MATCHCASE = wx._windows.FR_MATCHCASE
wxFR_REPLACEDIALOG = wx._windows.FR_REPLACEDIALOG
wxFR_NOUPDOWN = wx._windows.FR_NOUPDOWN
wxFR_NOMATCHCASE = wx._windows.FR_NOMATCHCASE
wxFR_NOWHOLEWORD = wx._windows.FR_NOWHOLEWORD
wxEVT_COMMAND_FIND = wx._windows.wxEVT_COMMAND_FIND
wxEVT_COMMAND_FIND_NEXT = wx._windows.wxEVT_COMMAND_FIND_NEXT
wxEVT_COMMAND_FIND_REPLACE = wx._windows.wxEVT_COMMAND_FIND_REPLACE
wxEVT_COMMAND_FIND_REPLACE_ALL = wx._windows.wxEVT_COMMAND_FIND_REPLACE_ALL
wxEVT_COMMAND_FIND_CLOSE = wx._windows.wxEVT_COMMAND_FIND_CLOSE
wxFindDialogEvent = wx._windows.FindDialogEvent
wxFindDialogEventPtr = wx._windows.FindDialogEventPtr
wxFindReplaceData = wx._windows.FindReplaceData
wxFindReplaceDataPtr = wx._windows.FindReplaceDataPtr
wxFindReplaceDialog = wx._windows.FindReplaceDialog
wxFindReplaceDialogPtr = wx._windows.FindReplaceDialogPtr
wxPreFindReplaceDialog = wx._windows.PreFindReplaceDialog
IDM_WINDOWTILE = wx._windows.IDM_WINDOWTILE
IDM_WINDOWTILEHOR = wx._windows.IDM_WINDOWTILEHOR
IDM_WINDOWCASCADE = wx._windows.IDM_WINDOWCASCADE
IDM_WINDOWICONS = wx._windows.IDM_WINDOWICONS
IDM_WINDOWNEXT = wx._windows.IDM_WINDOWNEXT
IDM_WINDOWTILEVERT = wx._windows.IDM_WINDOWTILEVERT
wxFIRST_MDI_CHILD = wx._windows.FIRST_MDI_CHILD
wxLAST_MDI_CHILD = wx._windows.LAST_MDI_CHILD
wxMDIParentFrame = wx._windows.MDIParentFrame
wxMDIParentFramePtr = wx._windows.MDIParentFramePtr
wxPreMDIParentFrame = wx._windows.PreMDIParentFrame
wxMDIChildFrame = wx._windows.MDIChildFrame
wxMDIChildFramePtr = wx._windows.MDIChildFramePtr
wxPreMDIChildFrame = wx._windows.PreMDIChildFrame
wxMDIClientWindow = wx._windows.MDIClientWindow
wxMDIClientWindowPtr = wx._windows.MDIClientWindowPtr
wxPreMDIClientWindow = wx._windows.PreMDIClientWindow
wxPyWindow = wx._windows.PyWindow
wxPyWindowPtr = wx._windows.PyWindowPtr
wxPrePyWindow = wx._windows.PrePyWindow
wxPyPanel = wx._windows.PyPanel
wxPyPanelPtr = wx._windows.PyPanelPtr
wxPrePyPanel = wx._windows.PrePyPanel
wxPyScrolledWindow = wx._windows.PyScrolledWindow
wxPyScrolledWindowPtr = wx._windows.PyScrolledWindowPtr
wxPrePyScrolledWindow = wx._windows.PrePyScrolledWindow
wxPrintoutTitleStr = wx._windows.PrintoutTitleStr
wxPreviewCanvasNameStr = wx._windows.PreviewCanvasNameStr
wxPRINT_MODE_NONE = wx._windows.PRINT_MODE_NONE
wxPRINT_MODE_PREVIEW = wx._windows.PRINT_MODE_PREVIEW
wxPRINT_MODE_FILE = wx._windows.PRINT_MODE_FILE
wxPRINT_MODE_PRINTER = wx._windows.PRINT_MODE_PRINTER
wxPRINT_MODE_STREAM = wx._windows.PRINT_MODE_STREAM
wxPrintData = wx._windows.PrintData
wxPrintDataPtr = wx._windows.PrintDataPtr
wxPageSetupDialogData = wx._windows.PageSetupDialogData
wxPageSetupDialogDataPtr = wx._windows.PageSetupDialogDataPtr
wxPageSetupDialog = wx._windows.PageSetupDialog
wxPageSetupDialogPtr = wx._windows.PageSetupDialogPtr
wxPrintDialogData = wx._windows.PrintDialogData
wxPrintDialogDataPtr = wx._windows.PrintDialogDataPtr
wxPrintDialog = wx._windows.PrintDialog
wxPrintDialogPtr = wx._windows.PrintDialogPtr
wxPRINTER_NO_ERROR = wx._windows.PRINTER_NO_ERROR
wxPRINTER_CANCELLED = wx._windows.PRINTER_CANCELLED
wxPRINTER_ERROR = wx._windows.PRINTER_ERROR
wxPrinter = wx._windows.Printer
wxPrinterPtr = wx._windows.PrinterPtr
wxPrinter_GetLastError = wx._windows.Printer_GetLastError
wxPrintout = wx._windows.Printout
wxPrintoutPtr = wx._windows.PrintoutPtr
wxPreviewCanvas = wx._windows.PreviewCanvas
wxPreviewCanvasPtr = wx._windows.PreviewCanvasPtr
wxPreviewFrame = wx._windows.PreviewFrame
wxPreviewFramePtr = wx._windows.PreviewFramePtr
wxPREVIEW_PRINT = wx._windows.PREVIEW_PRINT
wxPREVIEW_PREVIOUS = wx._windows.PREVIEW_PREVIOUS
wxPREVIEW_NEXT = wx._windows.PREVIEW_NEXT
wxPREVIEW_ZOOM = wx._windows.PREVIEW_ZOOM
wxPREVIEW_FIRST = wx._windows.PREVIEW_FIRST
wxPREVIEW_LAST = wx._windows.PREVIEW_LAST
wxPREVIEW_GOTO = wx._windows.PREVIEW_GOTO
wxPREVIEW_DEFAULT = wx._windows.PREVIEW_DEFAULT
wxID_PREVIEW_CLOSE = wx._windows.ID_PREVIEW_CLOSE
wxID_PREVIEW_NEXT = wx._windows.ID_PREVIEW_NEXT
wxID_PREVIEW_PREVIOUS = wx._windows.ID_PREVIEW_PREVIOUS
wxID_PREVIEW_PRINT = wx._windows.ID_PREVIEW_PRINT
wxID_PREVIEW_ZOOM = wx._windows.ID_PREVIEW_ZOOM
wxID_PREVIEW_FIRST = wx._windows.ID_PREVIEW_FIRST
wxID_PREVIEW_LAST = wx._windows.ID_PREVIEW_LAST
wxID_PREVIEW_GOTO = wx._windows.ID_PREVIEW_GOTO
wxPreviewControlBar = wx._windows.PreviewControlBar
wxPreviewControlBarPtr = wx._windows.PreviewControlBarPtr
wxPrintPreview = wx._windows.PrintPreview
wxPrintPreviewPtr = wx._windows.PrintPreviewPtr
wxPyPrintPreview = wx._windows.PyPrintPreview
wxPyPrintPreviewPtr = wx._windows.PyPrintPreviewPtr
wxPyPreviewFrame = wx._windows.PyPreviewFrame
wxPyPreviewFramePtr = wx._windows.PyPreviewFramePtr
wxPyPreviewControlBar = wx._windows.PyPreviewControlBar
wxPyPreviewControlBarPtr = wx._windows.PyPreviewControlBarPtr


d = globals()
for k, v in wx._windows.__dict__.iteritems():
    if k.startswith('EVT'):
        d[k] = v
    elif k.startswith('IDM'):
        d[k] = v
del d, k, v


