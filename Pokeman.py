#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2020_07_18.py
#  
#  Copyright 2020 Yuming Zeng <Yuming Zeng@SURFACE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
class Energe:
	def __init__(self, value):	# value [1, 3]
		self.Value = value
		
class Weapon:
	def __init__(self, value):	# value [1, 3]
		self.Value = value

class Pokeman:
	def __init__(self, name, health, damage):	# health = 50, damage = 5
		self.Name = name
		self.Health = health
		self.Damage = damage
	
	def EatEnerge(self, energe):
		self.Health = self.Health + energe.Value
		
	def Damange(self, otherPokeman):
		otherPokeman.Health = otherPokeman.Health - self.Damage
		if (otherPokeman.Health <= 0):
			otherPokeman.Die()
		
	def InstallWeapon(self, weapon):
		self.Damage = self.Damage + weapon.Value
		
	def Die(self):
		otherPokeman.Health = 0
		
# Game Rule
# - Starting with two Pokemans
# - Every round, there is one Pokeman active
#	The actie pokeman can type in an Energe, Weapon, or Damage request
#	This automatically generated energe/weapon/damage request will apply to the active Pokeman


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
