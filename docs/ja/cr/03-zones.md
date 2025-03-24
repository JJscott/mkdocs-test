[REF book=CR chap=3]

# Zones @@cha:zones@@



## General @@sec:zones_general@@


### A zone is a collection of objects. There are 15 types of zones: arms, arsenal, banished, chest, combat chain, deck, graveyard, hand, head, hero, legs, permanent, pitch, stack, and weapon.

#### @@rule:empty_exposed@@ A zone is considered empty when it does not contain any objects and has no permanents equipped to it. An equipment zone is exposed if it is empty. A zone does not cease to exist if it is empty.


### Each player has their own arms, arsenal, banished, chest, deck, graveyard, hand, head, hero, legs, and pitch zones; and has two weapon zones. The stack zone, permanent zone, and combat chain zone are shared by all players.

> **Note:** Cards printed before 2023 have used the phrase "zone you control" which refers to a zone that the player owns.


### @@rule:object_visibility@@ An object can have one of two possible states of visibility: public, or private. A public object is an object where information about the properties of the object is currently available to all players. A private object is an object where the information about the properties of that object is not currently available to all players.

#### A player may look at any private object they own, or is in a zone that they own, unless the object is in the deck zone.


### A public zone is a zone in which the default visibility of objects is public. A private zone is a zone in which the default visibility of objects is private.

#### The arms, banished, chest, combat chain, graveyard, head, hero, legs, permanent, pitch, stack, and weapon zones are public zones.

#### The arsenal, deck, and hand zones are private zones.

#### A public zone may contain a private object, if the object is made private while in that zone, or if the object is moved into that zone as a private object. The private object remains private until a rule or effect makes it public.

#### A private zone may contain public objects if the object is made public while in that zone, or if the object is moved into that zone as a public object. The public object remains public until a rule or effect makes it private.

#### @@rule:public_in_public_zone@@ If a rule or effect specifies an object in a public zone, the source must be public for the rule or effect to apply unless otherwise stated.

> **Example:** Tome of Torment has the text "You may play Tome of Torment from your banished zone." If a Tome of Torment is private (face-down) in the banished zone, a public zone, its ability would not apply because it does not explicitly state face-down.


### @@rule:arena@@ The arena is a collection of all the arms, chest, combat chain, head, hero, legs, permanent, and weapon zones.

#### The arena is not a zone. If an object would be put into the arena by a rule or effect without specifying a zone, it is placed into the permanent zone as a permanent.

#### The arsenal, banished, deck, graveyard, hand, pitch, and stack zones are not part of the arena.


### The layout and representation of zones and objects in those zones are defined by tournament rules.


### When an object moves from one zone to another, the object leaving its old zone (origin) and the object entering its new zone (destination) is performed simultaneously. At no point is the object not in a zone.

#### The object as it leaves the origin is considered the object moving for rules and effects. If the object is private when it moves zones, it is considered to have no properties for effects.

> **Example:** Levia has the text "While a card with 6 or more \{p\} has been put into your banished zone this turn, [...]," which is a while-conditional static effect. If a card is banished and it has 4 \{p\} as it leaves its origin, but 6 \{p\} when it enters the banished zone, it does not meet the condition of the effect. If a card is banished and it is private as it leaves its origin, it does not meet the condition of the effect.

#### If the origin and the destination of a move are the same, then no move occurs. If the object would go from public to private during the move, it just becomes private instead. If the object would go from private to public during the move, it just becomes public instead.

> **Example:** Mark of the Beast has the text "If this would be put into your graveyard from anywhere, instead banish it." If Mark of the Beast is banished face-down, and then an effect tries to put it into the graveyard, it will become face-up and remain in the banished zone. It is still considered the same card as before.


### @@rule:flip_step@@ If a private object will move zones and be public at the destination, it becomes public before it is moved. If a public object will move zones and be private at the destination, it becomes private before it is moved.

> **Example:** Azalea's activated ability puts a card from the deck (private object) into the arsenal face-up (public object in a private zone), therefore it becomes public before it is moved.

> **Example:** Intimidate puts a card from hand (private object) into the banished zone face down (private object in a public zone), therefore it does not become public before it is moved.

#### If the destination of an object is replaced after the object becomes public, then [[rule:flip_step]] is re-evaluated based on whether it will be a public or private object at the new destination.

> **Example:** Drone of Brutality has the text "If Drone of Brutality would be put into your graveyard from anywhere, instead put it on the bottom of your deck." If Drone of Brutality is discarded (from the private hand zone to the public graveyard zone), the card first becomes a public object, then the replacement effect replaces the destination to be the deck (a private zone), the card becomes a private object, and finally, the cards are moved to the bottom of the deck.


### @@rule:become_new_object@@ If an object enters a zone that is not in the arena and is not the stack zone, or a public object becomes a private object, it resets - its previous existence ceases to exist and it becomes a new object with no relation to its previous existence.

> **Example:** Endless Arrow is played and during the reaction step, Snapdragon Scalers is activated to give it "go again." Endless Arrow hits and returns to the player's hand (a zone outside the arena) and therefore becomes a new object. If the player plays Endless Arrow again it will not have "go again" because it is a new Endless Arrow card with no relation to its previous existence.

#### An ability that triggers when an object moves from one zone to another still references the new object, as long as the object remains a public object.

> **Example:** Merciful Retribution has the text "Whenever an aura or attack action card you control is destroyed, [...] If it's a non-token Light card, put it into your hero's soul." If a non-token Light card in the arena is destroyed, it moves to the graveyard and becomes a new object. However, because Merciful Retribution triggers on the object moving to the graveyard (as part of its destruction) it still references the new object it becomes in that zone for the triggered-layer it produces. If the non-token Light card moves to another zone or becomes private before the layer resolves, the triggered-layer loses that reference.

#### An ability with an effect that moves an object from one zone to another still references the new object for the remainder of any effects it generates, as long as the object remains a public object.

> **Example:** Bull's Eye Bracers has the text "If you have no cards in your arsenal, you may put an arrow card from your hand face up into your arsenal. It gains +1\{p\} until end of turn." If an arrow card is put into the arsenal, it becomes a new object. However, because the activated ability of Bull's Eye Bracers was the source of the effect that moved the arrow card, the rest of the effect still references the new object it became in that zone.

#### The process of how an object becomes a new object is preserved as the history of that new object.

> **Example:** Slithering Shadowpede has the text "If this was banished from your hand this turn, you may play it from your banished zone." If Slithering Shadowpede is banished from hand, it resets and becomes a new object in the banished zone, but the information regarding where it was banished from is preserved, allowing it to be played from the banished zone this turn.


### Zones of the same type are independent of their creation method. If a rule or effect creates a zone of the same type as an existing zone, the created zone is not distinguishable as being created by that rule or effect - only that there is now an additional zone of that type.

#### If a rule or effect moves an object into a specified type of zone, and there are two or more zones that match the specified type, the player that owns the object chooses which zone that object is moved to.

#### If the zone of a player ceases to exist, and there is only one of that type of zone owned by the player, any cards in that zone are cleared and the zone ceases to exist.

#### If the zone of a player ceases to exist, and there are two or more of that type of zone owned by the player, an empty zone of that type owned by the player ceases to exist. If there are no zones of that type owned by the player that are empty, the player chooses which zone will cease to exist - any cards in that zone are cleared and the zone ceases to exist.


### If a rule would move an object to a zone that does not exist, or the zone cannot contain that object, the object is cleared instead[[rule:clear_definition]]. If an effect would move an object to a zone that does not exist, or the zone cannot contain that object, and the object would not cease to exist from another rule or effect, then the move event fails.

> **Example:** Uzuri has the text "[...] put target attacking card with stealth from the active chain link on the bottom of its owner's deck [...]" If the target attacking card with stealth has the token type, it ceases to exist before it is put on the bottom of the deck.


### @@rule:clear_definition@@ To clear an object, move it from its current zone to its owner's graveyard.

#### If the object is a token, macro, or a non-card-layer, it leaves its current zone and simply ceases to exist.


### If an effect refers to one or more zones without specifying the owner of those zones (or specifying "any"), it refers to the zones owned by the controller of the effect.


### @@rule:under_definition@@ A sub-card is a card that is under a permanent, or a card on the stack. A top-card is the card on top, and the sub-card is underneath.

#### A card is only considered to be under a permanent if specified by a rule or effect.

#### A sub-card is not considered to be in the arena, even if its top-card is in the arena. If a card becomes a sub-card, it ceases to exist and becomes a new card with no relation to its previous existence[[rule:become_new_object]].

#### If a top-card moves zones and remains the same object, its sub-cards move to the same zone as part of the same event and remain sub-cards. If a top-card becomes a sub-card of another permanent, all of its sub-cards also become sub-cards of that permanent.

#### If the top-card is public, all sub-cards are also public. If a top-card is private, all sub-cards are also private.

#### If a top-card ceases to exist, its sub-cards are cleared as part of the same event.[[rule:clear_definition]]



## Arena @@sec:arena@@


### The arena is a collection of all the arms, chest, combat chain, head, hero, legs, permanent, and weapon zones.

#### The arsenal, banished, deck, graveyard, hand, pitch, and stack zones are not part of the arena.


### The arena is not a zone. If an object would be put into the arena by a rule or effect without specifying a zone, it is placed into the permanent zone as a permanent.

#### A card is considered to be in the arena if it is in any of the arena zones, and it is not a sub-card under permanent.



## Arms @@sec:arms_zone@@


### An arms zone is a public equipment zone in the arena, owned by a player.


### An arms zone can only contain up to one object which is equipped to that zone.[[rule:equip_effect]]

#### An object can only be equipped to an arms zone if it has subtype arms.


### A player may equip an arms card to their arms zone at the start of the game.[[sec:starting_a_game]]



## Arsenal @@sec:arsenal_zone@@


### An arsenal zone is a private zone outside the arena, owned by a player.


### An arsenal zone can only contain up to one of its owner's deck-cards.[[rule:deck_card]]

#### If an effect would put a card into an arsenal zone that is not empty, or into the arsenal and there are no empty arsenal zones, that effect fails.


### The term "arsenal" refers to all arsenal zones owned by a player and the cards in those zones.

#### A player's arsenal is considered empty if all of their arsenal zones are empty.

#### If a rule or effect would specify a card to move into a player's arsenal, it is moved into one of their empty arsenal zones.


### Cards in an arsenal zone may be played.[[sec:playing_cards]]



## Banished @@sec:banished_zone@@


### A banished zone is a public zone outside the arena, owned by a player.


### A banished zone can only contain its owner's cards.



## Chest @@sec:chest_zone@@


### A chest zone is a public equipment zone in the arena, owned by a player.


### A chest zone can only contain up to one object which is equipped to that zone.[[rule:equip_effect]]

#### An object can only be equipped to a chest zone if it has subtype chest.


### A player may equip a chest card to their chest zone at the start of the game.[[sec:starting_a_game]]



## Combat Chain @@sec:combat_chain_zone@@


### The combat chain zone is a public zone in the arena. There is only one combat chain zone, shared by all players, and it does not have an owner.


### The combat chain zone can only contain cards and attack-proxies[[rule:attack_proxy]].


### The term "combat chain" refers to the combat chain zone.


### The combat chain is "open" during combat - otherwise it is "closed."[[cha:combat]]



## Deck @@sec:deck_zone@@


### A deck zone is a private zone outside the arena, owned by a player.


### A deck zone can only contain its owner's deck-cards.[[rule:deck_card]]


### The term "deck" refers to the deck zone.


### A player cannot look at objects in their own deck zone unless specified by a rule or effect.


### Objects in the deck zone are placed face down in an ordered uniform pile.


### A player's starting deck starts the game in their deck zone.[[sec:starting_a_game]]



## Graveyard @@sec:graveyard_zone@@


### A graveyard zone is a public zone outside the arena, owned by a player.


### A graveyard zone can only contain its owner's cards.


### The term "graveyard" refers to the graveyard zone.



## Hand @@sec:hand_zone@@


### A hand zone is a private zone outside the arena, owned by a player.


### A hand zone can only contain its owner's deck-cards.[[rule:deck_card]]


### The term "hand" refers to the hand zone.



## Head @@sec:head_zone@@


### A head zone is a public equipment zone in the arena, owned by a player.


### A head zone can only contain up to one object which is equipped to that zone.[[rule:equip_effect]]

#### An object can only be equipped to a head zone if it has subtype head.


### A player may equip a head card to their head zone at the start of the game.[[sec:starting_a_game]]



## Hero @@sec:hero_zone@@


### A hero zone is a public zone in the arena, owned by a player.


### A hero zone can only contain one card, with the type hero, and zero or more cards in the hero's soul.


### The term "hero" refers to the card with the type hero in the hero zone.


### A player must start the game with their hero card in their hero zone.[[sec:starting_a_game]]


### @@rule:hero_soul@@ A hero's soul refers to the collection of sub-objects under the hero card.[[rule:under_definition]]



## Legs @@sec:legs_zone@@


### A legs zone is a public equipment zone in the arena, owned by a player.


### A legs zone can only contain up to one object which is equipped to that zone.[[rule:equip_effect]]

#### An object can only be equipped to a legs zone if it has subtype legs.


### A player may equip a legs card to their legs zone at the start of the game.[[sec:starting_a_game]]



## Permanent @@sec:permanent_zone@@


### The permanent zone is a public zone in the arena. There is only one permanent zone, shared by all players, and it does not have an owner.


### The permanent zone can only contain permanents.



## Pitch @@sec:pitch_zone@@


### A pitch zone is a public zone outside the arena, owned by a player.


### A pitch zone can only contain its owner's deck-cards.[[rule:deck_card]]



## Stack @@sec:stack_zone@@


### The stack zone is a public zone outside the arena. There is only one stack zone, shared by all players, and it does not have an owner.


### The term "stack" refers to the stack zone.


### The stack contains an ordered collection of layers.[[sec:layers]]


### When a layer is added onto the stack, it becomes layer N+1 where N is the number of existing layers on the stack.


### The top layer of the stack is layer N, with the highest value of N.


### When a layer N is removed from the stack by a rule or effect, any layer M where M>N becomes layer M-1.

> **Example:** There are 4 layers on the stack. Layer 2 is an instant card and is removed by a "negate" effect. Layer 3 becomes layer 2, and layer 4 becomes layer 3, while layer 1 remains unchanged.



## Weapon @@sec:weapon_zone@@


### A weapon zone is a public zone in the arena, owned by a player.


### A weapon zone can only contain up to one object which is equipped to that zone.[[rule:equip_effect]]

#### An object can only be equipped to a weapon zone if it has the type weapon or the subtype off-hand or quiver. An object with the subtype 2H must be equipped to two weapon zones.[[rule:2h_subtype]]


### A player may equip a weapon card or an off-hand card to their weapon zone at the start of the game.[[sec:starting_a_game]]
