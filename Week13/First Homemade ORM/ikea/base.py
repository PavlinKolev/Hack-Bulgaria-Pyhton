from ikea.fields import BaseColumn


class DateBaseMeta(type):
    def __new__(cls, name, bases, clsdict):
        # import ipdb; ipdb.set_trace()
        fields = {}
        for attr, value in clsdict.items():
            if isinstance(value, BaseColumn):
                fields[attr] = value

        for key, value in fields.items():
            clsdict.pop(key)

        clsdict['_fields'] = fields

        obj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(obj, '_registry'):
            setattr(obj, '_registry', set())
        else:
            obj._registry.add(obj)

        return obj
