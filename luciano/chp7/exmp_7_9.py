def tag(name, *content, class_=None, **attrs):
    """Сгенерировать один или несколько HTML тегов"""
    if class_ is not None:
        attrs['class'] = class_
    attrs_pairs = (f' {attr}="{value}"' for attr, value
                   in sorted(attrs.items()))
    attr_str = ''.join(attrs_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
                    for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'
