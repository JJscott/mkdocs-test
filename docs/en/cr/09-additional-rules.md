---
title: Comprehesive Rules – Additional Rules
description: "Additional rules that cover unique mechanics outside of the general rules."
document: cr
chapter: 9
---

# Additional Rules @@cha:additional_rules@@



## General @@sec:addiitonal_rules_general@@



## Double-Faced Cards @@sec:double_faced_cards@@


### A double-faced card is a card with two sets of properties - each set printed as a separate face on the card.


### Each face of a double-faced card has its own set of printed properties.

#### If a player may look at a double-faced card, they may look at both faces of the card.

#### If an effect instructs a player to name a card[[rule:name_effect]], they may name one side of a double-faced card, but not both.

#### If an effect applies to a double-faced card, it continues to apply to the card even if its properties are defined by a different face, as long as it does not cease to exist between changing properties.

> **Example:** Oasis Respite has the text "Prevent the next 4 damage that would be dealt to target hero this turn by a source of your choice." If a flip-card card with its front-face active is chosen as the source, then the flip-card resolves, enters the arena, and its back-face becomes active, it is still subjected to Oasis Respite's effect.


### @@rule:flip_card@@ A flip-card is a double-faced card that has a front-face and a back-face, with one of the following printed subtypes on its front-face: figment, invocation, or construct. Only one face of a flip-card is active at any given point. The properties of a flip-card are defined by its active face. The types of its front-face determines if it is a hero-, token-, deck-, or arena-card[[sec:cards]].

#### If a flip-card is outside the game, its front-face is active.

#### If a flip-card is inside the game, its front-face is active until a rule or effect would make its back-face active. If the card would then become a new card, its front-face is active again.[[rule:become_new_object]]

> **Example:** Construct Nitro Mechanoid is the front-face of a flip-card. When it resolves on the stack, its Construct subtype rules that it enters the arena with its back face active, turning it into Nitro Mechanoid. If it is destroyed and moves to the graveyard, it becomes a Construct Nitro Mechanoid again because its front-face is active.


### @@rule:twin_card@@ A twin-card is a double-faced card that has two faces. One or both faces of a twin-card may be active at any given point. The properties of a twin-card are defined by its active face(s). The combination of the types of both its faces determines if it is a hero-, token-, deck-, or arena-card[[sec:cards]].

#### If a twin-card is outside the arena and not on the stack, both of its faces are active.

> **Example:** Levia, Redeemed // Blasmophet, Levia Consumed is a twin-card with the text "Action -- Turn all cards in your banished zone face-down: Transform into Levia, Redeemed. Activate this ability only while this is in your inventory and you have 13 or more cards with blood debt in your banished zone." and "While this is in your inventory, when blood debt reduces your \{h\} to 13, you may transform into Blasmophet, Levia Consumed." respectively. While this card is in a player's inventory, both of these abilities are functional because the card as a whole has both sets of properties from both its faces.

#### If a twin-card is in the arena or on the stack, only one of its faces is active. Its active face is determined by the player that played it, or by the effect that put it into the arena or on the stack.


### @@rule:transcend_card@@ A transcend-card is a double-faced card that has a front-face and a back-face, with the front-face that has an ability that generates the transcend effect[[rule:transcend_effect]]. Only one face of a transcend-card is active at any given point. The properties of a transcend-card are defined by its active face. The types of its front-face determines if it is a deck- or arena-card[[sec:cards]].

#### If a transcend-card is outside the game, its front-face is active.

#### If a transcend-card is inside the game, its front-face is active until it transcends and makes its back-face active. Its back-face remains active even if it would become a new object.[[rule:become_new_object]]

> **Example:** Stir the Pot is the front-face of a transcend-card. When it resolves, and transcends, its Inner Chi back-face becomes the active face and it is put into its owner's hand. For the remainder of the game, it will continue to be Inner Chi, whether it is pitched, discarded, banished, etc.



## Split-Cards @@sec:split_cards@@


### A split-card is a card with two names, typeboxes, and textboxes - each printed on different sides of the card.


### A split-card is considered a single card with all the properties of both sides, except when put onto the stack[[rule:split_card_on_stack]].

> **Example:** Comet Storm||Shock is a single card with two names ("Comet Storm" and "Shock"), two supertypes (Lightning and Wizard), two types (Instant and Action), and two sets of abilities.

#### A split-card can only be included in a player's card-pool if the supertypes of both sides are a subset of their hero's supertypes[[rule:player_card_pool]].

> **Example:** A player can only include Comet Storm||Shock if their hero has the Lightning and Wizard supertypes.

#### If an effect instructs a player to name a card[[rule:name_effect]], they may name one of the two split-card names, but not both.


### @@rule:split_card_on_stack@@ When a split-card is put onto the stack, the player that puts it there chooses one of its two sides[[rule:play_split_card]]. For the remainder of its existence, it is considered to have only the name, typebox, and textbox of the chosen side. The other side's name, typebox, and textbox are considered to not exist.

> **Example:** Comet Storm||Shock is a split card. If the player chooses the left side, the card only has the name Comet Storm, the typebox "Wizard Action," and textbox "Deal 5 arcane damage to any target." If the player chooses the right side, the card only has the name Shock, the typebox "Lightning Instant," and textbox "Deal 1 arcane damage to any target."



## Marked @@sec:marked@@


### Marked is a special condition that a hero may have.


### A hero is marked if an effect causes them to be marked[[rule:mark_effect]]

#### If an effect would cause a marked hero to become marked, they continue to be marked.

#### A marked hero continues to be marked until they are hit by a source controlled by an opponent or they cease to exist.


### When a marked hero is hit by a source controlled by an opponent[[rule:hit]], the marked condition of that hero is removed as part of the hit event. The removal of the marked condition is not a game state-process or a triggered effect.
