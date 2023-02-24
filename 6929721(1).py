#List of cars available
Cars={"toyotaSequoia":250000,
      "hyundaiCreta":200000,
      "hyundaiVenue":300000,
      "hyundaiTucson":300000,
      "hyundaiVen":450000,
      "hyundaiVerna":300000,
      "hyundaiAlcazar":300000,
      "hyundaiXcentSentra":500000,
      "toyotaCamry":200000,
      "nissanAltima":355000,
      "toyotaCorolla":30000,
      "nissanRogue":450000,
      "toyotaPrius":25000,
      "toyotaYaris":150000,
      "toyotaFortuner":500000,
      "toyota4Runner":800000,
      "toyotaAvanza":450000,
      "nissanKicks":250000,
      "toyotaSienna":320000,
      "nissanMicra":330000,
      "nissanPathfinder":455000,
      "toyotaHighlander":377000,
      "toyotaAvalon":350000,
      "nissanAlmera":550000,
      "nissanNavara":550000,
      "nissanArmada":650000,
      "nissanPatrol":450000,
      "nissanSunny":245000,
      "nissanAriya":335000,
      "nissanQuest":745000,
      "nissanZ":430000,
      "nissanTitan":125000}


#request for car
carName=input("Type name of car")

if carName in Cars:
    print("car available")
    
    
elif carName not in Cars:
    print("car not available")
    
    
#https://github.com/kbdasampong/Data-structures.git
    
