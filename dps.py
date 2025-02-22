import numpy as np
import matplotlib.pyplot as plt

version = "INDEV-v0.6.1"
calcExceptions = []
print("generated using OSPUZE™ Finals Stats Calculator", version)

userInput = input("Load stats of an existing / example weapon? (y/n): ")
if(userInput == "y"):
    print("List of live weapons:\n Light: V9S, M11, XP-54, LH1, SR-84 \n Medium: Turret, R.357, AKM, FCAR, FAMAS, Pike-556 \n Heavy: .50 Akimbo, M60, Lewis Gun, KS-23")
    print("List of hypothetical weapons:\n Light: N/A \n Medium: N/A \n Heavy: N/A")
    selectedWeapon = input("Weapon: ")
    match selectedWeapon:
        #Hypothetical Weapons:
        #Light:
        #Medium:
        #Heavy:
        #Live Weapons:
        #Light:
        case "V9S":
            damage = 40.0
            critMulti = 1.5
            firerate = 360 / 60
            magazine = 20
            rangeDamageModifer = 0.67
            falloffStart = 10
            falloffEnd = 15
        case "M11":
            damage = 16
            critMulti = 1.5
            firerate = 1000 / 60
            magazine = 40
            rangeDamageModifer = 0.62
            falloffStart = 10
            falloffEnd = 15
        case "XP-54":
            damage = 16.0
            critMulti = 1.5
            firerate = 850 / 60
            magazine = 34
            rangeDamageModifer = 0.62
            falloffStart = 20
            falloffEnd = 30
        case "LH1":
            damage = 46.0
            critMulti = 2.0
            firerate = 270 / 60
            magazine = 15
            rangeDamageModifer = 0.72
            falloffStart = 50
            falloffEnd = 55
        case "SR-84":
            damage = 118.0
            critMulti = 2.0
            firerate = 40 / 60
            magazine = 6
            rangeDamageModifer = 0.75
            falloffStart = 80
            falloffEnd = 100
        #Medium:
        case "Turret":
            calcExceptions = ["Limited Range", "Inf Ammo", "No Crit", "No Falloff"]
            damage = 5.0
            firerate = 480 / 60
            maxRange = 20
        case "R.357":
            damage = 74.0
            critMulti = 2
            firerate = 140 / 60
            magazine = 6
            rangeDamageModifer = 0.45
            falloffStart = 23
            falloffEnd = 40
        case "AKM":
            damage = 20.0
            critMulti = 1.5
            firerate = 600 / 60
            magazine = 32
            rangeDamageModifer = 0.45
            falloffStart = 35
            falloffEnd = 40
        case "FCAR":
            damage = 22.0
            critMulti = 1.5
            firerate = 540 / 60
            magazine = 25
            rangeDamageModifer = 0.55
            falloffStart = 35
            falloffEnd = 40
        case "FAMAS":
            calcExceptions = ["Burst"]
            damage = 23.0
            critMulti = 1.5
            firerate = 1080 / 60
            burstCount = 3
            burstDelay = 1 / (220  / 60)
            magazine = 27
            rangeDamageModifer = 0.5
            falloffStart = 35
            falloffEnd = 47.5
        case "Pike-556":
            damage = 50.0
            critMulti = 1.5
            firerate = 200 / 60
            magazine = 12
            rangeDamageModifer = 0.85
            falloffStart = 50
            falloffEnd = 55
        #Heavy:
        case ".50 Akimbo":
            damage = 44.0
            critMulti = 2.0
            firerate = 230 / 60
            magazine = 14
            rangeDamageModifer = 0.5
            falloffStart = 37.5
            falloffEnd = 50
        case "M60":
            damage = 19.0
            critMulti = 1.5
            firerate = 580 / 60
            magazine = 70
            rangeDamageModifer = 0.4
            falloffStart = 25
            falloffEnd = 32.5
        case "Lewis Gun":
            damage = 22.0
            critMulti = 1.5
            firerate = 500 / 60
            magazine = 47
            rangeDamageModifer = 0.67
            falloffStart = 35
            falloffEnd = 40
        case "KS-23":
            calcExceptions = ["No Crit"]
            damage = 100.0
            firerate = 73 / 60
            magazine = 6
            rangeDamageModifer = 0.7
            falloffStart = 18
            falloffEnd = 23
    
    if not("No Crit" in calcExceptions):
        critDamage = damage * critMulti
    if not("No Falloff" in calcExceptions):
        rangedDamage = damage * rangeDamageModifer
    if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
        rangedCritDamage = critDamage * rangeDamageModifer


    secondsPerShot = 1 / firerate
    if not("Inf Ammo" in calcExceptions):
        secondsToEmpty = magazine / firerate

    print("Damage:", damage)
    if not("No Crit" in calcExceptions):
        print("Crit Multiplier:", critMulti)
        print("Damage w/ Crit:", round(critDamage, 3))
    if not("No Falloff" in calcExceptions):
        print("Ranged Damage Modifier:", rangeDamageModifer)
        print("Falloff start distance:", falloffStart)
        print("Falloff end distance:", falloffEnd)
        print("Damage @Range:", round(rangedDamage, 3))
    else:
        print("Range: {}m".format(maxRange))
    if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
        print("Damage @Range w/ Crit:", round(rangedCritDamage, 3))

    print("")

    print("RPM:", round(firerate * 60, 2))
    if ("Burst" in calcExceptions):
        print("Burst Delay: {}s".format(burstDelay))
        print("Shots per Burst:", burstCount)
    if not("Inf Ammo" in calcExceptions):
        print("Magazine:", magazine)
        print("Seconds to empty: {}s".format(round(secondsToEmpty, 3)))
    else:
        print("Magazine: Inf")

else:
    damage = float(input("Damage: "))
    userInput = input("Input crit damage directly? (y/n): ")
    if(userInput == "y"):
        critDamage = float(input("Damage w/ Crit: "))
    else:
        critMulti = float(input("Crit Multiplier: "))
        critDamage = damage * critMulti
        print("Damage w/ Crit:", round(critDamage, 3))

    rangeDamageModifer = float(input("Ranged Damage Modifier: "))
    falloffStart = float(input("Falloff start distance: "))
    falloffEnd = float(input("Falloff end distance: "))
    rangedDamage = (damage * rangeDamageModifer)
    print("Damage @Range:", round(rangedDamage, 3))
    rangedCritDamage = (critDamage * rangeDamageModifer)
    print("Damage w/ Crit @Range:", round(rangedCritDamage, 3))

    print("")

    firerate = float(input("RPM: ")) / 60
    secondsPerShot = 1 / firerate
    magazine = int(input("Magazine: "))
    if ("Burst" in calcExceptions):
        ##TODO
        print("Seconds to empty is not available for Burst weapons in the current version ({})".format(version))
    else:
        secondsToEmpty = (magazine / firerate)
        print("Seconds to empty: {}s".format(round(secondsToEmpty, 3)))

print("")

dps = damage * firerate
if not("Inf Ammo" in calcExceptions):
    damagePotential = damage * magazine
else:
    damagePotential = "Inf"
if not("No Crit" in calcExceptions):
    critDamagePotential = critDamage * magazine
    critDps = (critDamage * firerate)
if not("No Falloff" in calcExceptions):
    rangedDamagePotential = (rangedDamage * magazine)
    rangedDps = dps * rangeDamageModifer
if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
    rangedCritDamagePotential = (rangedCritDamage * magazine)
    rangedCritDps = critDps * rangeDamageModifer

#TODO
if not("Burst" in calcExceptions):
    print("DPS:", round(dps, 3))
    if not("No Crit" in calcExceptions):
        print("DPS w/ Crit:", round(critDps, 3))
    if not("No Falloff" in calcExceptions):
        print("DPS @Range:", round(rangedDps, 3))
    if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
        print("DPS w/ Crit @Range", round(rangedCritDps, 3))
else:
    #TODO
    print("DPS information is not available for Burst weapons in the current version ({})".format(version))
print("")

if not("Inf Ammo" in calcExceptions):
    print("Damage Potential:", round(damagePotential, 3))
else:
    print("Damage Potential: Inf")
if not("No Crit" in calcExceptions):
    print("Damage Potential /w Crit:", round(critDamagePotential, 3))
if not("No Falloff" in calcExceptions):
    print("Damage Potential @Range:", round(rangedDamagePotential, 3))
if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
    print("Damage Potential /w Crit @Range:", round(rangedCritDamagePotential, 3))

print("")

def measureSTK(damage, hp, damageOrSTK = 1):
    i = 1
    while True:
        if((i * damage) >= hp):
            if damageOrSTK == 0:
                return(i * damage)
            else:
                return(i)
        i += 1
        
def measureTTK(damage, secondsPerShot, hp):
    shotsToKill = measureSTK(damage, hp)
    if ("Burst" in calcExceptions):
        #TODO
        return("PLACEHOLDER")
    else:
        return(secondsPerShot * (shotsToKill - 1))

def measureDamage(damage, rangeDamageModifier, falloffStart, falloffEnd, distance):
    if(distance <= falloffStart):
        return(damage)
    elif(distance >= falloffEnd):
        return(damage * rangeDamageModifier)  # Minimum damage after falloff ends
    else:
        percentage = (distance - falloffStart) / (falloffEnd - falloffStart)
        return(damage * (1 - percentage * (1 - rangeDamageModifier)))

def outputCombatInfo(build, damage, secondsPerShot):
    match build:
        case "Light":
            return("{} damage in {}s using {} shots".format(round(measureSTK(damage, 150, 0), 3), round(measureTTK(damage, secondsPerShot, 150), 3), measureSTK(damage, 150)))
        case "Medium":
            return("{} damage in {}s using {} shots".format(round(measureSTK(damage, 250, 0), 3), round(measureTTK(damage, secondsPerShot, 250), 3), measureSTK(damage, 250)))
        case "Heavy":
            return("{} damage in {}s using {} shots".format(round(measureSTK(damage, 350, 0), 3), round(measureTTK(damage, secondsPerShot, 350), 3), measureSTK(damage, 350)))

print("TTK, STK, and Damage dealt to all classes (ignoring reloads since that isn't implemented yet):\n")

print("Against Light:", outputCombatInfo("Light", damage, secondsPerShot))
if not("No Crit" in calcExceptions):
    print("Against Light w/ Crit:", outputCombatInfo("Light", critDamage, secondsPerShot))
if not("No Falloff" in calcExceptions):
    print("Against Light @Range:", outputCombatInfo("Light", rangedDamage, secondsPerShot))
if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
    print("Against Light w/ Crit @Range:", outputCombatInfo("Light", rangedCritDamage, secondsPerShot))

print("")

print("Against Medium:", outputCombatInfo("Medium", damage, secondsPerShot))
if not("No Crit" in calcExceptions):
    print("Against Medium w/ Crit:", outputCombatInfo("Medium", critDamage, secondsPerShot))
if not("No Falloff" in calcExceptions):
    print("Against Medium @Range:", outputCombatInfo("Medium", rangedDamage, secondsPerShot))
if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
    print("Against Medium w/ Crit @Range:", outputCombatInfo("Medium", rangedCritDamage, secondsPerShot))

print("")

print("Against Heavy:", outputCombatInfo("Heavy", damage, secondsPerShot))
if not("No Crit" in calcExceptions):
    print("Against Heavy w/ Crit:", outputCombatInfo("Heavy", critDamage, secondsPerShot))
if not("No Falloff" in calcExceptions):
    print("Against Heavy @Range:", outputCombatInfo("Heavy", rangedDamage, secondsPerShot))
if not("No Crit" in calcExceptions) and not("No Falloff" in calcExceptions):
    print("Against Heavy w/ Crit @Range:", outputCombatInfo("Heavy", rangedCritDamage, secondsPerShot))

if not("No Falloff" in calcExceptions):
    print("\nDamage numbers at all falloff values:")
    xpoints = [damage, damage, rangedDamage, rangedDamage]
    xpoints = np.array(xpoints)

    ypoints = [0, falloffStart, falloffEnd, 100]
    ypoints = np.array(ypoints)

    plt.plot(ypoints, xpoints, marker = 'o')

    plt.title(selectedWeapon)
    plt.xlabel("Distance")
    plt.ylabel("Damage")

    plt.show()