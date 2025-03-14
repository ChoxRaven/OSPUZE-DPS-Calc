import json
from dataclasses import dataclass, field, fields
from typing import Dict, List, Optional
from pathlib import Path


@dataclass
class Weapon:
    name: str
    damage: float
    critMulti: float
    magazine: int
    falloffStart: float
    falloffEnd: float
    falloffMulti: float
    bps: int
    shotFrames: float
    reloadFrames: int
    time_between_shots: float = 1.0
    time_between_full_reload: float = 1.0
    burstFrames: Optional[float] = None
    time_between_bursts: Optional[float] = None
    fps: float = 120
    falloff_multipliers: List = field(default_factory=list) 
    
    def __post_init__(self):
        self.time_between_shots = self.shotFrames / self.fps
        self.time_between_full_reload = self.reloadFrames / self.fps
        if self.burstFrames is not None:
            self.time_between_bursts = self.burstFrames / self.fps

        self.calculate_falloff_multipliers(2)
    
    def calculate_falloff_multipliers(self, range_samples: int):
        falloff_scale = (1 - self.falloffMulti) / range_samples
        self.falloff_multipliers = [self.falloffMulti + (falloff_scale * num) for num in range(range_samples + 1)]
        self.falloff_multipliers.reverse()


@dataclass
class WeaponStats:
    current_magazine: int = 0
    shots: int  = 0
    reloads: int  = 0
    ttk: float  = 0
    final_dmg: float  = 0
    weapon_dict: Dict = field(default_factory=dict)
    
    def reset_stats(self):
        self.shots = 0
        self.reloads = 0
        self.ttk = 0
        self.final_dmg = 0
    
    def create_stat_dict(self, weapon_name: str, contestant_name: str, falloff: int, crit: int):
        
        if weapon_name not in self.weapon_dict:
            self.weapon_dict[weapon_name] = {}
        
        if contestant_name not in self.weapon_dict[weapon_name]:
            self.weapon_dict[weapon_name][contestant_name] = {}
        
        if falloff not in self.weapon_dict[weapon_name][contestant_name]:
            self.weapon_dict[weapon_name][contestant_name][falloff] = {}
        
        if crit not in self.weapon_dict[weapon_name][contestant_name][falloff]:
            self.weapon_dict[weapon_name][contestant_name][falloff][crit] = {}
        
        for field_info in fields(self):
            if field_info.type is Dict:
                continue
            
            var_value: str = getattr(self, field_info.name)
            self.weapon_dict[weapon_name][contestant_name][falloff][crit][field_info.name] = var_value
    
    def export_stats(self, weapon_name: str):
        with open(f'F:/WD/OSPUZE-DPS-Calc/weapons/{weapon_name}.json', 'w+') as file:
            json.dump(self.weapon_dict, file, indent=4)
        
    def print_stats(self, contestant_name: str, falloff: int, crit: int):
            for var_name, var_value in self.weapon_dict[contestant_name][falloff][crit].items():
                print(var_name, var_value)
                

# Create Weapon dataclass instances
weapon_v9s = Weapon(
    name='v9s',
    damage=40.0,
    critMulti=1.5,
    magazine=27,
    falloffStart=10,
    falloffEnd=15,
    falloffMulti=0.67,
    bps=1,
    shotFrames=20,
    reloadFrames=180,
)

weapon_famas = Weapon(
    name='famas',
    damage=23,
    critMulti=1.5,
    magazine=27,
    falloffStart=35,
    falloffEnd=47.5,
    falloffMulti=0.5,
    bps=3,
    shotFrames=19,
    reloadFrames=312,
    burstFrames=9,
    
)

weapon_akm = Weapon(
    name='akm',
    damage=30,
    critMulti=1.5,
    magazine=32,
    falloffStart=30,
    falloffEnd=37.5,
    falloffMulti=0.55,
    bps=1,
    shotFrames=15,
    reloadFrames=282,
)