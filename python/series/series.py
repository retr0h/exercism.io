def slices(digits, size):
    series = map(int, list(digits))
    if not size or size > len(series):
        raise ValueError()

    return [series[i:i + size]
            for i, _ in enumerate(series) if i + size <= len(series)]
