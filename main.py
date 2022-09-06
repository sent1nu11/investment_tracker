import investpy

date_start = '01/01/2020'
date_end = '23/12/2021'

# INDICES
SET = investpy.indices.get_index_historical_data(index="set", country="Thailand", from_date= date_start, to_date=date_end, as_json=False,
                                                 order='ascending', interval='Daily')
print(SET)

print(investpy.funds.get_fund_countries())

print(investpy.funds.get_funds_list())

# MUTUAL FUNDS

# print(investpy.funds.get_funds_dict())

fund = investpy.funds.get_fund_historical_data(
    fund='Calvert Emerging Markets Equity Fund Class I',
    country='united states',
    from_date= date_start,
    to_date=date_end,
    as_json=False,
    order='ascending',
    interval='Daily'
)

print(fund)