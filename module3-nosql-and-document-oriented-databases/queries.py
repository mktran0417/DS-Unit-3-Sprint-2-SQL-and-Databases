TOTAL_CHARACTERS = 'SELECT COUNT(character_id) FROM charactercreator_character;'
TOTAL_SUBCLASS = '''
                    SELECT COUNT(*) FROM (SELECT *
                    FROM charactercreator_character cc_c
                    INNER JOIN charactercreator_necromancer cc_n
                    ON cc_c.character_id = cc_n.mage_ptr_id);
                 '''
TOTAL_ITEMS = '''
                    SELECT COUNT(cc_ci.id)
                    FROM charactercreator_character as cc_char
                    INNER JOIN charactercreator_character_inventory as cc_ci
                    WHERE cc_char.character_id = cc_ci.character_id;
                '''
TOTAL_WEAPON = '''
                    SELECT COUNT(*)
                    FROM charactercreator_character AS cc_char
                    INNER JOIN charactercreator_character_inventory AS cc_ci
                    ON cc_char.character_id = cc_ci.character_id
                    INNER JOIN armory_weapon AS aw
                    WHERE aw.item_ptr_id = cc_ci.item_id
                '''
NON_WEAPONS = ''''''
CHARACTER_ITEMS = ''''''
CHARACTER_WEAPONS = ''''''
AVG_CHARACTER_ITEMS = ''''''
AVG_CHARACTER_WEAPONMS = ''''''

GET_CHARACTERS = '''
        SELECT * FROM charactercreator_character
    '''
GET_CHARACTERS_ITEMS =  '''
                        SELECT name, value, weight
                        FROM charactercreator_character_inventory as cc_ci
                        LEFT JOIN armory_item
                        WHERE cc_ci.item_id = armory_item.item_id and armory_item.item_id < 138 and cc_ci.character_id = {}
                        '''

GET_CHARACTERS_WEAPONS = '''
                            SELECT name, value, weight
                            FROM charactercreator_character_inventory as cc_ci
                            LEFT JOIN armory_item
                            ON cc_ci.item_id = armory_item.item_id
                            INNER JOIN armory_weapon
                            where armory_weapon.item_ptr_id = cc_ci.item_id and cc_ci.character_id = {}
                         '''
