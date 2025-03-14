from dataclasses import dataclass

from weapons.weapon_dataclasses import Weapon
from weapons.weapon_dataclasses import WeaponStats
from weapons.weapon_dataclasses import weapon_famas

@dataclass
class Contestant:
    name: str
    health: int


def weapon_fire(weapon: Weapon, weapon_stats: WeaponStats, weapon_crit: float, contestant: Contestant, falloff_mp: float): #type: ignore
    """
    Calculate weapon fire for each bullet

    Args:
        weapon (Weapon): Weapon Dataclass
        weapon_crit (float): Weapon Crit
        contestant (Contestant): Contestant Dataclass
        falloff_mp (float): Falloff Multiplier

    Returns:
        WeaponStats: Weapon Statistics for the parsed crit and falloff multipliers
    """
    weapon_stats.reset_stats()
    weapon_stats.current_magazine = weapon.magazine
    current_hp = contestant.health    
    damage = weapon.damage * weapon_crit * falloff_mp
       
    for _ in range(weapon_stats.current_magazine):            
        for _ in range(weapon.bps):
            if weapon_stats.current_magazine <= 0:
                weapon_stats.reloads += 1
                weapon_stats.ttk += weapon.time_between_full_reload
                weapon_stats.current_magazine = weapon.magazine
                
            weapon_stats.shots += 1
            weapon_stats.current_magazine -= 1
            weapon_stats.final_dmg += damage
            
            current_hp -= damage
            if current_hp <= 0:
                return weapon_stats
            
            if weapon.time_between_bursts:
                weapon_stats.ttk += weapon.time_between_bursts
        
        weapon_stats.ttk += weapon.time_between_shots


def calculate_weapon_damage(weapon: Weapon, contestant: Contestant): 
    weapon_stats = WeaponStats()
    
    for i, fallof_mp in enumerate(weapon.falloff_multipliers):
        for j, crit in enumerate([1, weapon.critMulti]):
            weapon_fire(weapon, weapon_stats, crit, contestant, fallof_mp)
            weapon_stats.create_stat_dict(weapon.name, contestant.name, i, j)
    
    #weapon_stats.print_stats(contestant.name, 2, 0)
    weapon_stats.export_stats(weapon.name)

if __name__ == '__main__':

    # Create Contestant dataclass instances
    contestant_heavy = Contestant('heavy', 350)
    contestant_medium = Contestant('medium', 250)
    contestant_light = Contestant('light', 150)

    
    
    calculate_weapon_damage(weapon_famas, contestant_heavy)
    #calculate_weapon_damage(weapon_famas, contestant_light)