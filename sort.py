hotbar= [
    'torch',
    'rock',
    'potion',
    'sword',
    'shield'
]

index = hotbar.index('potion')
item = hotbar.pop(index)
hotbar.insert(0, item)
print(hotbar)