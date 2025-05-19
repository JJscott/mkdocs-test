---
title: FAB Comprehensive Rules – Object Properties
description: A complete overview of the properties that make up an object.
document: cr
chapter: 2
---

# Object Properties @@cha:object_properties@@



## General @@sec:object_properties_general@@


### A property is an attribute of an object that defines how the object interacts with the rules and effects of the game. There are 13 properties an object may have: abilities[[sec:abilities]], color strip, cost, defense, intellect, life, name, pitch, power, subtypes, supertypes, text box, and type.

#### An ability is a property, not an object. However, activated abilities have the object properties cost and type, for the purposes of rules and effects.


### The properties of a card are defined by the information printed on the official Flesh and Blood card. If a property is not printed on the official Flesh and Blood card, the card it represents does not have that property.

#### @@rule:card_errata@@ If an errata has been published for a given card, the properties of that card are defined by the corrections in that errata. (See [http://fabtcg.com/errata](http://fabtcg.com/errata))


### @@rule:numeric_property@@ A numeric property is a property that has a numeric value. The value of some numeric properties can be modified by effects and/or counters to produce a modified value. The copyable value of the numeric property is typically the value that the object starts its existence with.

#### An effect that modifies the value of a numeric property does not modify the base value of that property unless otherwise specified by the effect.

> **Example:** An effect that specifies an object to "gain," "get," "have," or "lose" a property-related value, modifies the value of the property but does not change the base value unless it specifically uses the term "base."

#### A numeric property is considered to have increased or decreased if a rule or effect is applied that causes an increase or decrease to its base or modified value[[rule:continuous_effect_event]].

> **Example:** Korshem, Crossroads of the Elements has the text "[...], if [...] no card or token controlled by a hero has had \{p\} or \{d\} increased this turn, destroy Korshem, Crossroads of the Elements." If a player plays a card and an effect applies to the card that increases its power, a card controlled by a hero has had its power increased and Korshem will not be destroyed.

#### A numeric property cannot have a negative base or modified value. If one or more effects would set or reduce the base or modified value of a numeric property to be less than zero, instead they set or reduce it to zero.

#### A +1 or -1 property-related counter on an object, modifies the value of the property but does not change the base value.


### An object is considered to have gained a property, or part of a property, if it did not have that property/part before, but currently does. An object is considered to have lost a property, or part of a property, if it had that property/part but currently does not.


### @@rule:property_source@@ The source of a property is the object of which the property is an attribute.



## Color Strip @@sec:color_strip@@


### Color Strip is a visual representation of the printed pitch of a card.


### The color strip of a card is typically located at the top of a card. The printed pitch of a card determines the color strip of the card. Cards with a printed pitch of 1, 2, and 3, typically have a color strip of red, yellow, and blue respectively. A card with no printed pitch typically does not have a color strip.
* A card with a red color strip is considered red for the purposes of rules and effects.
* A card with a yellow color strip is considered yellow for the purposes of rules and effects.
* A card with a blue color strip is considered blue for the purposes of rules and effects.


### If the base pitch or pitch of a card is modified, it does not modify the color strip of the card.



## Cost @@sec:cost@@


### Cost is a numeric property of a card or ability, which determines the starting resource asset-cost to play the card or activate the ability.[[rule:play_calculate_asset]]


### The printed cost of a card is typically expressed within a resource point symbol located in the top right corner of the card. The printed cost defines the base cost of a card. If a card does not have a printed cost, it does not have the cost property (0 is a valid printed cost).

#### If the printed value is expressed as two or more undefined symbols and/or numeric values, they are additive for determining the base cost of a card.

> **Example:** Spark of Genius has the cost property with the printed value of "XX," which determines the base cost as X+X for any value of X.


### The printed cost of an activated ability is expressed as \{r\} symbols as part of the description of the ability, where the number of \{r\} symbols dictates the printed cost. If there are no resource symbols, then the printed cost is 0. The printed cost defines the base resource cost of the ability.[[rule:activated_ability_definition]]


### The cost property of an object cannot be modified.

#### An effect that increases or reduces the cost of an object does not modify the cost property of that object. Effects that modify cost are only applied as part of the process for playing or activating that object.[[rule:play_calculate_asset]]

> **Example:** An effect that reduces the cost to play a card does not change the cost property of that card in any way - it only changes the calculation of the resource cost when that card is being played.

#### An effect that refers to the cost of an object refers to the unmodified cost property of an object. An effect that refers to the payment of an object, refers to the modified cost of an object when it was paid to play/activate and put that object on the stack.


### The visual expression in \{r\} symbols and the numerical expression of cost are functionally identical.

> **Example:** The text "Search your deck for a card with cost value 1," is considered to be the same as the text "Search your deck for a card with cost value \{r\}."



## Defense @@sec:defense@@


### Defense is a numeric property of an object, which represents the value contributed to the total sum of defense used in the damage step of combat.[[sec:damage_step]]


### The printed defense of a card is typically located at the bottom right corner of a card next to the \{d\} symbol. The printed defense defines the base defense of a card. If a card does not have a printed defense, it does not have the defense property (0 is a valid printed defense).

#### If the defense of a card is represented as a (c), then the card has an ability that defines the defense of the card at any point in or out of the game. If the ability requires a number that cannot be determined, the defense of the card is 0.


### The defense of an object can be modified. The term "defense" or the symbol \{d\} refers to the modified defense of an object.



## Intellect @@sec:intellect@@


### Intellect is a numeric property of a hero card, which represents the number of cards the controlling player draws up to at the end of their turn.[[sec:end_phase]]


### The printed intellect of a card is typically located at the bottom left corner of a card next to the \{i\} symbol. The printed intellect defines the base intellect of a card. If a card does not have a printed intellect, it does not have the intellect property (0 is a valid printed intellect).


### The intellect of an object can be modified. The term "intellect" or the symbol \{i\} refers to the modified intellect of an object.



## Life @@sec:life@@


### @@rule:living_object@@ Life is a numeric property of an object, which represents the starting life total of that object. An object with the life property is a living object.


### The printed life of a card is typically located at the bottom right corner of a card next to the \{h\} symbol. The printed life defines the base life of a card. If a card does not have a printed life, it does not have the life property (0 is a valid printed life).


### @@rule:life_total@@ The life of an object can be modified. The term "life total" or the symbol \{h\} refers to the modified life of an object.

#### An object's life total is equal to the object's base life, plus life gained and minus life lost, as recorded by the players of the game.

#### Life gained and life lost are not continuous effects - they are discrete effects that apply once, and they permanently modify the life total.[[rule:gain_asset_effect]]

#### If the base life of an object changes, then the life total is recalculated using the new base life value of the object.

> **Example:** Shiyana has 20 base life and the text "[...] Shiyana becomes a copy of target hero [...]." If Shiyana has lost 5 life and copies the target hero is Kano, with 15 base life, the new life total for Shiyana is 10.

#### An object's life total can be greater than its base life.

#### An object cannot have a negative life total. If the life total is calculated to be less than zero, instead it is considered zero.

#### If a living object's life total is reduced to zero, it is cleared as a game state action; or if the living object is a hero, their player loses or the game is a draw as a game state action.[[rule:game_state_action]][[sec:ending_a_game]]

#### @@rule:die@@ If a living object ceases to exist, it is considered to have died.



## Metatype @@sec:metatypes@@


### Metatypes are a collection of metatype keywords. The metatypes of an object determine whether it may be added to a game.


### An object can have zero or more metatypes.


### The metatype of a card is determined by its type box. The metatype is printed before the card's supertypes.


### The metatypes of an activated-layer or triggered-layer are the same as the metatypes of its source.


### An object cannot gain or lose metatypes.


### Metatypes are either hero-metatypes or set-metatypes. Hero-metatypes specify the moniker(s) of a hero, and the card can only be included in a player's card-pool if it matches their hero's moniker(s). Set-metatypes specify the the name(s) of the set the object can be used in as defined by tournament rules.

#### The set-metatypes are Rosetta.
Subtypes are either functional or non-functional keywords. Functional subtypes add additional rules to an object[[sec:subtype_keywords]]. Non-functional subtypes do not add additional rules to an object.



## Name @@sec:name@@


### Name is a property of an object, which represents one of its object identities and determines the object's uniqueness (along with the pitch property).[[rule:object_identity]][[rule:distinct_card]]


### @@rule:define_name@@ The printed name of a card is typically located at the top of the card. The printed name defines the name of a card.


### @@rule:define_moniker@@ If an object has a name that is a personal name, that name determines the object's moniker - the most significant identifier of the object's name. A personal name is typically written in the format "[HONORIFIC?] [MONIKER] [LAST?] [, SUFFIX?]," where HONORIFIC (if any) is one or more name honorifics, MONIKER is the moniker of the name, LAST (if any) is one or more middle and/or last names, and SUFFIX (if any) is a title or nickname written after a comma.

> **Example:** The monikers of these names are as follows: Bravo (Bravo), Dorinthea Ironsong (Dorinthea), Data Doll MKII (Data Doll), Ser Boltyn, Breaker of Dawn (Boltyn), Blasmophet, the Soul Harvester, (Blasmophet), The Librarian (The Librarian), Dawnblade (Dawnblade), Stalagmite, Bastion of Isenloft (Stalagmite).

#### If an object does not have a name that is a personal name, it does not have a moniker.

#### If two objects have different names, they may have the same moniker. An effect that refers to an object using a moniker may refer to two or more objects with different names but the same moniker.

> **Example:** The cards "Bravo," "Bravo, Showstopper," and "Bravo, Star of the Show," all have the moniker "Bravo."

#### A moniker is not considered a name. If an effect identifies an object by a name, it does not identify objects with a moniker that is the same as that name.

> **Example:** If a player is instructed by an effect to name a card and they declare "Dawnblade," the effect identifies cards with the name "Dawnblade," but not cards with the name "Dawnblade, Resplendent" despite them having the moniker "Dawnblade."


### An object's printed name is always considered to be the English language version of its name, regardless of the printed language.


### A name or part of a name is equal to another name or part of a name only if it is an exact case-insensitive match.

> **Example:** Censor has the text "When this hits a hero, name a card. They can't play the named card until the end of their next turn." If the named card is "Blazing Aether", the effect would not prevent the player from playing "Trailblazing Aether."



## Pitch @@sec:pitch@@


### Pitch is a property of a card, which represents the assets a player gains when they pitch the card. The pitch value of the card is the number of assets gained when pitched and it determines the object's uniqueness (along with the name property).[[rule:pitching]][[rule:distinct_card]]


### The printed pitch of a card is expressed visually as one, two, or three socketed \{r\} or \{c\} symbols, typically located in the top left corner of a card, where the types of symbols dictate what asset is generated when pitched and the number of symbols dictates the printed pitch value. The printed pitch value defines the base pitch value of a card. If a card does not have a printed pitch value, it does not have the pitch property.


### The pitch of an object can be modified. The term "pitch" refers to the modified pitch value of an object.


### The visual expression of \{r\} or \{c\} symbols and the numerical expression of pitch are functionally identical.

> **Example:** The text "Search your deck for a card with pitch value 1," is considered to be the same as the text "Search your deck for a card with pitch value \{r\}."



## Power @@sec:power@@


### Power is a numeric property of an object, which represents the power value used in the damage step of combat.[[sec:damage_step]]


### The printed power of a card is typically located at the bottom left corner of a card next to the \{p\} symbol. The printed power defines the base power of a card. If a card does not have a printed power, it does not have the power property (0 is a valid printed power).

#### If the power value of a card is represented as a (c) then the card has an ability that defines the base power of the card at any point in or out of the game. If the ability requires a number that cannot be determined, the power of the card is 0.


### The power of an object can be modified. The term "power" or the symbol \{p\} refers to the modified power of an object.



## Subtypes @@sec:subtypes@@


### Subtypes are a collection of subtype keywords. The functional subtypes of a card determine what additional rules apply to the card.


### An object can have zero or more subtypes.


### The subtypes of a card are determined by its type box. Subtypes (if any) are printed after a long dash after the card's type.


### The subtypes of an activated-layer or triggered-layer are the same as the subtypes of its source.


### An object can gain or lose subtypes from rules and/or effects.


### Subtypes are either functional or non-functional keywords. Functional subtypes add additional rules to an object[[sec:subtype_keywords]]. Non-functional subtypes do not add additional rules to an object.

#### The functional subtype keywords are (1H), (2H), Affliction, Ally, Arrow, Ash, Attack, Aura, Construct, Figment, Invocation, Item, Landmark, and Quiver.[[sec:subtype_keywords]]

#### The non-functional subtypes keywords are Angel, Arms, Axe, Base, Book, Bow, Brush, Chest, Chi, Claw, Club, Dagger, Demon, Dragon, Evo, Fiddle, Flail, Gem, Gun, Hammer, Head, Legs, Lute, Mercenary, Off-Hand, Orb, Pistol, Rock, Scepter, Scroll, Scythe, Shuriken, Song, Staff, Sword, Trap, Wrench, and Young.



## Supertypes @@sec:supertypes@@


### Supertypes are a collection of supertype keywords. The supertypes of a card determine whether a card can be included in a player's card-pool.


### An object can have zero or more supertypes.


### The supertypes of a card are determined by its type box. Supertypes are printed before the card's type (if any).


### The supertypes of an activated-layer or triggered-layer are the same as the supertypes of its source.


### An object can gain or lose supertypes from rules and/or effects.


### Supertypes are non-functional keywords and do not add additional rules to an object. A supertype is either a class or a talent.

#### @@rule:class_supertype_keywords@@ The class supertype keywords are Adjudicator, Assassin, Bard, Brute, Guardian, Illusionist, Mechanologist, Merchant, Ninja, Ranger, Runeblade, Shapeshifter, Warrior, and Wizard.

#### @@rule:talent_supertype_keywords@@ The talent supertype keywords are Chaos, Draconic, Earth, Elemental, Ice, Light, Lightning, Mystic, Royal, and Shadow.



## Text Box @@sec:text_box@@


### The text box of a card contains the card text of a card, typically located on the lower half of a card beneath the illustration.


### The card text of a card contains the rules text, reminder text, and flavor text of the card (if any). Rules text is printed in roman and boldface. Reminder text is printed in parenthesized italics. Flavor text is separated vertically from the rules and reminder text (if any) by a horizontal bar and is printed in italics.


### The rules text of a card defines the base abilities of the card. A paragraph of rules text typically defines a single ability. Reminder and flavor text do not affect the game.

#### @@rule:self_reference_text@@ If the rules text specifies the name and/or moniker of its source object in the third-person it is a self-reference. A self-reference can be interpreted as "this" and it refers to its source object and not other cards with the same name.

#### @@rule:object_creation_and_reference_text@@ If the rules text specifies the name and/or moniker of another object in the context of creating it, it refers to a hypothetical object with defined properties, including that name[[sec:token_keywords]]. Otherwise, if the rules text specifies the name and/or moniker of another object it refers to any existing object with that name and/or moniker.



## Traits @@sec:traits@@


### Trait is a property of an object, which represents one of its object identities.[[rule:object_identity]]


### @@rule:define_trait@@ The printed traits of a card are typically located at the top of the card, under the card name. The printed traits define the traits of a card.


### Traits are non-functional keywords or phrases and do not add additional rules to an object.

#### @@rule:trait_keywords@@ The trait keywords and phrases are Agents of Chaos.


### If an effect refers to a group of cards by a trait, it refers to all cards with that trait.

> **Example:** Arakni, Web of Deceit has the text "At the beginning of your end phase, if an opponent is marked, you become a random Agent of Chaos." This refers to a group which includes all cards with the Agent of Choas trait, and selecting one at random from that group.



## Type Box @@sec:type_box@@


### The type box of a card determines the card's metatypes, supertypes, types, and subtypes, typically located at the bottom of the card. Type boxes are typically written in the format "[METATYPES] [SUPERTYPES] [TYPE] [--- SUBTYPES]," where METATYPES is zero or more metatypes, SUPERTYPES is zero or more supertypes, TYPE is zero or more types, and SUBTYPES is zero or more subtypes.

#### @@rule:generic_definition@@ If the SUPERTYPES of a type box is "Generic," the card has no supertypes.

#### @@rule:hybrid_definition@@ Hybrid cards are cards with SUPERTYPES written in the format "[SUPERTYPES-1] / [SUPERTYPES-2]." A hybrid card can be included in a player's card-pool as though it only has one of the supertypes sets, SUPERTYPES-1 or SUPERTYPES-2, not both[[rule:player_card_pool]]. Otherwise, hybrid cards have all of the supertypes specified by SUPERTYPES-1 and SUPERTYPES-2.



## Types @@sec:types@@


### Types are a collection of type keywords. The types of a card determine whether the card is a hero-, token-, deck-, or arena-card, and how a deck-card may be played.


### An object can have zero or more types.


### The type of a card is determined by its type box. The type is printed after the card's supertypes, and before a long dash and subtypes (if any).


### The types of an activated-layer or triggered-layer are the same as the types of its source.

#### The types of an activated ability layer include the types determined by the activated ability.[[rule:activated_ability_definition]]


### An object can gain or lose types from rules and/or effects.


### Types are functional keywords and add additional rules to an object.[[sec:types]]

#### The type keywords are Action, Attack Reaction, Block, Defense Reaction, Demi-Hero, Equipment, Hero, Instant, Macro, Mentor, Resource, Token, and Weapon.[[sec:type_keywords]]
