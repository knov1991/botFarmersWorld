import requests_html

porcentoSaque = 0.94 # 0.94 = 6% taxa de saque // usar valor*porcentoSaque
cicloStoneAxe = 33 #usos/horas
cicloFishingRod = 50 #usos/horas
stoneAxeFarm = 1.7
fishingRodFarm = 5

session = requests_html.HTMLSession()
r = session.get('https://wax.alcor.exchange/trade/fww-farmerstoken_wax-eosio.token')
r.html.render(sleep=15, timeout=15)
for item in r.html.xpath("//*[contains(@class,'orders-list blist bids')]"):
    FWW = float(item.text[0]+item.text[1]+item.text[2]+item.text[3]+item.text[4])
    FWW = round(FWW, 3)

session = requests_html.HTMLSession()
r = session.get('https://wax.alcor.exchange/trade/fwg-farmerstoken_wax-eosio.token')
r.html.render(sleep=15, timeout=15)
for item in r.html.xpath("//*[contains(@class,'orders-list blist bids')]"):
    FWG = float(item.text[0]+item.text[1]+item.text[2]+item.text[3]+item.text[4])+0.01
    FWG = round(FWG, 3)

session = requests_html.HTMLSession()
r = session.get('https://wax.alcor.exchange/trade/fwf-farmerstoken_wax-eosio.token')
r.html.render(sleep=15, timeout=15)
for item in r.html.xpath("//*[contains(@class,'orders-list blist bids')]"):
    FWF = float(item.text[0]+item.text[1]+item.text[2]+item.text[3]+item.text[4])+0.01
    FWF = round(FWF, 3)

session = requests_html.HTMLSession()
r = session.get('https://www.binance.com/en/trade/WAXP_BUSD')
r.html.render(sleep=5, timeout=15)
for item in r.html.xpath("//*[contains(@class,'bid-light')]"):
    waxBusd = float(item.text)

session = requests_html.HTMLSession()
r = session.get('https://www.binance.com/en/trade/BUSD_BRL')
r.html.render(sleep=5, timeout=15)
for item in r.html.xpath("//*[contains(@class,'bid-light')]"):
    busdBrl = float(item.text)

print('FWW: '+str(FWW), 'FWG: '+str(FWG), 'FWF: '+str(FWF), 'WAX>BUSD: '+str(waxBusd), 'BUSD>BRL: '+str(busdBrl))
cicloStoneAxeDolar = ((cicloStoneAxe*stoneAxeFarm*porcentoSaque*FWW) - (20*FWG + 33*FWF)) * waxBusd
cicloStoneAxeBrl = cicloStoneAxeDolar*busdBrl
print('Lucro Stone Axe')
print('~1 ciclo/33h\n'+'$: ',round(cicloStoneAxeDolar, 2),'\nR$:',round(cicloStoneAxeBrl, 2))
print('~1 semana/5ciclos\n'+'$: ',round(cicloStoneAxeDolar*5, 2),'\nR$:',round(cicloStoneAxeBrl*5, 2))
print('~1 mês/20ciclos\n'+'$: ',round(cicloStoneAxeDolar*20, 2),'\nR$:',round(cicloStoneAxeBrl*20, 2))

cicloFishingRodDolar = ((cicloFishingRod*fishingRodFarm*porcentoSaque*FWF) - (50*FWG)) * waxBusd
cicloFishingRodBrl = cicloFishingRodDolar*busdBrl
print('\nLucro Fishing Rod')
print('~1 ciclo/50h\n'+'$: ',round(cicloFishingRodDolar, 2),'\nR$:',round(cicloFishingRodBrl, 2))
print('~1 semana/3ciclos\n'+'$: ',round(cicloFishingRodDolar*3, 2),'\nR$:',round(cicloFishingRodBrl*3, 2))
print('~1 mês/14ciclos\n'+'$: ',round(cicloFishingRodDolar*14, 2),'\nR$:',round(cicloFishingRodBrl*14, 2))