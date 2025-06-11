def generate_hashtags(title, description):
    text = (title + ' ' + description).lower()
    tags = []

    if any(word in text for word in ['ui', 'ux', 'дизайн', 'figma', 'product']):
        tags.append('#designer')
    if 'frontend' in text:
        tags.append('#frontend')
    if 'backend' in text:
        tags.append('#backend')
    if 'android' in text or 'ios' in text:
        tags.append('#mobile')
    if 'маркетинг' in text or 'smm' in text:
        tags.append('#marketing')
    if 'аналитик' in text or 'data' in text:
        tags.append('#analytics')

    return ' '.join(tags) if tags else '#job'