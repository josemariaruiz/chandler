"""Observable data structures -- see ``models.txt`` for docs"""

from events import Event

__all__ = ['Set', 'SetChanged']


class Set(object):
    """Observable collection of unordered unique objects"""

    __slots__ = 'data','type','__weakref__'

    def __init__(self,iterable=(),type=object):
        self.data = list(iterable)
        self.type = type

    def add(self,ob):
        """Add ``ob`` to contents and generate event if new item"""
        self.replace((),(ob,))

    def remove(self,ob):
        """Remove ``ob`` from contents and generate event if it was present"""
        self.replace((ob,))

    def reset(self,iterable=()):
        """Empty the set, then add items in ``iterable``, if supplied"""
        self.replace(list(self),iterable)

    def subscribe(self,receiver,hold=False):
        """Shortcut for ``SetChanged.subscribe(set,receiver,hold)``"""
        SetChanged.subscribe(self,receiver,hold)

    def unsubscribe(self,receiver):
        """Shortcut for ``SetChanged.unsubscribe(set,receiver)``"""
        SetChanged.unsubscribe(self,receiver)

    def replace(self,remove=(),add=()):
        """Remove items in ``remove``, add items in ``add``, generate events"""
        data = self.data
        added = []
        removed = []
        if add and self.type is not object:
            t = self.type
            for ob in add:
                if not isinstance(ob,t):
                    raise TypeError("%s is not a %s" % (ob,self._typeName(t)))
        if remove:
            for ob in remove:
                if ob in data:
                    data.remove(ob)
                    removed.append(ob)
        if add:
            for ob in add:
                if ob not in data:
                    data.append(ob)
                    added.append(ob)
        if removed or added:
            try:
                SetChanged(self,removed,added)
            except:
                map(data.remove,added)
                map(data.append,removed)
                SetChanged(self,added,removed)
                raise

    def _typeName(self,t):
        if isinstance(t,tuple):
            return '/'.join([typ.__name__ for typ in t])
        else:
            return t.__name__
            
    def __repr__(self):
        r = "Set(%r)" % self.data
        if self.type is not object:
            r = r[:-1]+ (', type=%s)' % self._typeName(self.type))
        return r

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)


class SetChanged(Event):
    """Set has changed membership"""

    __slots__ = 'added','removed'

    def __init__(self,sender,removed,added,**kw):
        self.added = added
        self.removed = removed
        super(SetChanged,self).__init__(sender,**kw)

    def __repr__(self):
        return "<Change for %r: removed=%r, added=%r>" % (
            self.sender, self.removed, self.added
        )
