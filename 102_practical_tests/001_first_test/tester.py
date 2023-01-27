seconds = 1234412
years = seconds // (24 * 3600 * 365)
seconds %= 24 * 3600 * 365
days = seconds // (24 * 60 * 60)
seconds %= (24 * 60 * 60)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{years}:{days}:{hours}:{minutes}:{seconds}')