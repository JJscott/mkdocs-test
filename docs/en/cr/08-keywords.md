---
title: Comprehesive Rules – Keywords
description: "A descriptions of all keywords: type, subtype, ability, label, effect, and token."
document: cr
chapter: 8
---

# Keywords @@cha:keywords@@



## General @@sec:keywords_general@@


### A keyword is a reserved term or phrase that serves as a descriptive element for rules and/or effects to reference or has some rules meaning.


### @@rule:type_keyword@@ A type keyword is a keyword used by a card's text box to describe the type of an object.


### @@rule:subtype_keyword@@ A subtype keyword is a keyword used by a card's text box to describe the subtype of an object.


### @@rule:ability_keyword@@ An ability keyword is a keyword that substitutes for the rules text of an ability.


### @@rule:label_keyword@@ A label keyword is a keyword that groups abilities with common effects. A label keyword and its ability are typically written in the format "[KEYWORD] - [ABILITY]."


### @@rule:effect_keyword@@ An effect keyword is a keyword that substitutes for the rules text of an effect.

#### When a discrete keyword effect is generated, or when a continuous effect is applied, it produces a corresponding event of that keyword.


### @@rule:token_keyword@@ A token keyword is a keyword that refers to a specific token. A token keyword is typically written in the format "[KEYWORD] token."



## Type Keywords @@sec:type_keywords@@


### **Action** @@rule:action_type@@
An action card is a deck-card.[[rule:deck_card]]

#### An action card/activated ability can only be played/activated when the stack is empty.

#### An action card/activated ability cannot be played/activated during combat, except during the Resolution Step of combat.[[rule:actions_during_combat]]

#### An action card/activated ability has the additional asset-cost of one action point to play/activate.[[rule:play_calculate_asset]]

#### @@rule:action_as_instant@@ If an action card/activated ability is played/activated as though it were an instant, it is still considered an action, but it can be played/activated any time the player has priority and does not cost an action point.


### **Attack Reaction** @@rule:attack_reaction_type@@
An attack reaction card is a deck-card.[[rule:deck_card]]

#### An attack reaction card/activated ability can only be played/activated by a player who controls an attacking hero during the Reaction Step of combat.[[sec:reaction_step]]

#### When an attack reaction card resolves as a layer on the stack, it is cleared.[[rule:clear_definition]]

#### An attack reaction card/activated ability is considered to be a reaction card/ability.


### **Defense Reaction** @@rule:defense_reaction_type@@
A defense reaction card is a deck-card.[[rule:deck_card]]

#### A defense reaction card/activated ability can only be played/activated by a player who controls a defending hero during the Reaction Step of combat.[[sec:reaction_step]]

#### When a defense reaction card resolves as a layer on the stack, it becomes a defending card on the active chain link.[[rule:defending_card]]

#### A defense reaction card/activated ability is considered to be a reaction card/ability.


### **Equipment** @@rule:equipment_type@@
An equipment card (without any other types) is an arena-card.[[rule:arena_card]]

#### As an arena-card, a player may equip an equipment card from their card-pool during the start-of-game procedure to its respective zone.[[sec:starting_a_game]]

#### An equipment permanent may be declared as a defending card during the Defend Step of combat.[[rule:declare_defense]]


### **Hero** @@rule:hero_type@@
A hero card is a hero-card[[rule:hero_card]]

#### A player starts the game with their hero card as a permanent in their hero zone.[[sec:starting_a_game]]

#### A hero card is separate from, and cannot be included in a player's, card-pool.[[rule:player_card_pool]]


### **Instant** @@rule:instant_type@@
An instant card is a deck-card.[[rule:deck_card]]

#### A card/activated ability with the type instant can be played/activated any time the player has priority.


### **Resource** @@rule:resource_type@@
A resource card is a deck-card.[[rule:deck_card]]

#### A resource card cannot be played.


### **Token** @@rule:token_type@@
A token card is a token-card.[[rule:token_card]]

#### Tokens only exist in the arena or as sub-cards[[rule:under_definition]]. If a token leaves the arena and it is not a sub-card, it ceases to exist.


### **Weapon** @@rule:weapon_type@@
A weapon card is an arena-card.[[rule:arena_card]]

#### As an arena-card, a player may equip a weapon card from their card-pool during the start-of-game procedure to its respective zone.[[sec:starting_a_game]]


### **Mentor** @@rule:mentor_type@@
A mentor card is a deck-card.[[rule:deck_card]]

#### A mentor card can only be included in a player's card-pool if they have a young (subtype) hero.


### **Demi-Hero** @@rule:demi_hero_type@@
A demi-hero card is an arena-card.[[rule:arena_card]]

#### A demi-hero card is distinct from a hero-card. It is included as part of a player's card-pool and it cannot be used in place of a player's hero at the start of the game.

#### If a demi-hero becomes a permanent in the arena and the controlling player does not control a hero, the demi-hero is considered to be that player's hero and has the hero type for the purposes of rules and effects for the rest of the game. Otherwise, if the player already controls a hero, the demi-hero is cleared from the arena[[rule:clear_definition]].


### **Block** @@rule:block_type@@
A block card is a deck-card.[[rule:deck_card]]

#### A block card cannot be played.


### **Macro** @@rule:macro_type@@
A macro is not a card.

#### Only macro objects have the macro type.[[sec:macros]]



## Subtype Keywords @@sec:subtype_keywords@@


### **(1H)** @@rule:1h_subtype@@

#### A (1H) object considered to be a one-hander.

#### A one-hander permanent must be equipped to a player's weapon zone. A one-hander cannot be equipped if the player does not have an empty weapon zone.


### **(2H)** @@rule:2h_subtype@@

#### A (2H) object considered to be a two-hander.

#### A two-hander permanent must be equipped to two of a player's weapon zones. A two-hander cannot be equipped if the player does not have two empty weapon zones.

#### A two-hander occupies either of the two weapon zones it is equipped to, but not both.


### **Attack** @@rule:attack_subtype@@

#### An attack card is considered an attack when on the stack or when it is on the combat chain as an attacking card.[[rule:attack_card]]

#### When an attack card is played, the combat chain opens (if it is closed) and the layer step of combat begins.[[sec:layer_step]]


### **Aura** @@rule:aura_subtype@@

#### When an aura resolves as a layer on the stack, it enters the arena.

#### When an aura enters the arena, it becomes a permanent, except when it is added as a defending card to a chain link.


### **Item** @@rule:item_subtype@@

#### When an item resolves as a layer on the stack, it enters the arena.

#### When an item enters the arena, it becomes a permanent, except when it is added as a defending card to a chain link.


### **Arrow** @@rule:arrow_subtype@@

#### An arrow can only be played from the player's arsenal and only if they control a bow.


### **Trap** @@rule:trap_subtype@@

> **Note:** As of 2023, trap is no longer a functional subtype keyword.


### **Ally** @@rule:ally_subtype@@

#### If an ally permanent ceases to exist, it is considered to have died.[[rule:die]]

#### During the End Phase, an ally's life total is reset to its base life.[[sec:end_phase]]

#### If an ally is attacking, the controlling player and their hero are not considered an attacking hero for that chain link; and the player cannot play or activate attack reaction cards or abilities during the reaction step of combat.[[rule:attacking_hero]]

#### If an ally is the target of an attack, the controlling player and their hero are not considered a defending hero for that chain link; and the player cannot declare defending cards or play or activate defense reaction cards or abilities during the reaction step of combat[[rule:defending_hero]]

#### If an ally deals damage, the controlling player and their hero are not considered to have dealt damage.

#### If an ally is dealt damage, the controlling player and their hero are not considered to have been dealt damage.


### **Landmark** @@rule:landmark_subtype@@

#### When a landmark resolves as a layer on the stack, it enters the arena.

#### When a landmark enters the arena, it becomes a permanent and all other landmark permanents are cleared, except when the landmark is added as a defending card to a chain link.[[rule:clear_definition]]


### **Off-Hand** @@rule:off_hand_subtype@@

#### An off-hand permanent must be equipped to a player's weapon zone. An off-hand cannot be equipped if the player does not have an empty weapon zone.

#### A player cannot equip more than one off-hand.


### **Affliction** @@rule:affliction_subtype@@

#### When an affliction resolves as a layer on the stack, it enters the arena.

#### When an affliction enters the arena, it becomes a permanent, except when it is added as a defending card to a chain link.

#### As an object with the subtype affliction enters the arena as a permanent, its controller declares an opponent and the object enters the arena under that player's control. If the affliction has no controller before it enters the arena, its owner declares the opponent. If the object cannot enter the arena under that player's control, it is cleared and is not considered to have entered the arena.


### **Ash** @@rule:ash_subtype@@

#### When an ash resolves as a layer on the stack, it enters the arena.

#### When an ash enters the arena, it becomes a permanent, except when it is added as a defending card to a chain link.


### **Invocation** @@rule:invocation_subtype@@

#### When an invocation resolves as a layer on the stack, it enters the arena with its back-face active and becomes a permanent.[[sec:double_faced_cards]]


### **Construct** @@rule:construct_subtype@@

#### When a construct resolves as a layer on the stack, it enters the arena with its back-face active and becomes a permanent.[[sec:double_faced_cards]]


### **Quiver** @@rule:quiver_subtype@@

#### A quiver permanent must be equipped to a player's weapon zone. A quiver may be equipped to, and occupy, a weapon zone that a two-hander bow is already equipped to but does not occupy; otherwise, a quiver cannot be equipped if the player does not have an empty weapon zone.

#### A player cannot equip more than one quiver.


### **Figment** @@rule:figment_subtype@@

#### When a figment resolves as a layer on the stack, it enters the arena.

#### When a figment enters the arena, it becomes a permanent, except when it is added as a defending card to a chain link.



## Ability Keywords @@sec:ability_keywords@@


### **Attack** @@rule:attack_ability@@
Attack is a static ability. A layer with the attack ability is an attack-proxy.

#### When an attack-proxy resolves on the stack, it and its source move onto the combat chain as a chain link.[[rule:attack_step_attack_proxy]]

#### If attack-proxy is added to the stack, the combat chain opens (if it is closed) and the Layer Step of combat begins.[[sec:layer_step]]

#### To add an attack-proxy onto the stack, a legal attackable target must be declared as the target of the attack.[[rule:attackable_target]]


### **Battleworn** @@rule:battleworn_ability@@
Battleworn is triggered-static ability that means "When the combat chain closes, if this defended, put a -1\{d\} counter on it."


### **Blade Break** @@rule:blade_break_ability@@
Blade Break is a triggered-static ability that means "When the combat chain closes, if this defended, destroy it."


### **Dominate** @@rule:dominate_ability@@
Dominate is a static ability that means "This can't be defended by more than one card from hand."

#### If an attack with dominate is currently defended by a card from hand, an additional card cannot be added as a defending card to the attack's chain link if the card comes from a player's hand.[[rule:defense_reaction_fail]][[rule:add_defend_effect]]

#### If an attack with dominate is currently defended by a card from hand on the activate chain link, defense reaction cards cannot be played from hand.[[rule:defense_reaction_cant_play]]

#### If an attack is defended by two or more cards from hand and then the attack gains dominate, no cards are retroactively removed from defending.


### **Go again** @@rule:go_again_ability@@
Go again is a special resolution ability that means "Gain 1 action point."

#### If go again is an ability of a non-attack layer on the stack, the controlling player gains 1 action point after all other resolution abilities have resolved.[[rule:resolve_go_again]]

#### If go again is an ability of an attack on the active chain link, the controlling player gains 1 action point at the beginning of the Resolution Step of combat.[[rule:combat_go_again]]

#### An object cannot have more than one "go again" ability. If an effect would give the "go again" ability to an object that already has the "go again" ability, then that part of the effect fails.


### **Legendary** @@rule:legendary_ability@@
Legendary is a meta-static ability that means "You may only have 1 of this in your constructed deck."


### **Specialization** @@rule:specialization_ability@@
Specialization is a meta-static ability. Specialization is written as "[HERO] Specialization" which means "You may only have this in your deck if your hero is [HERO]," where HERO is the moniker of the player's hero card.[[rule:define_moniker]]


### **Arcane Barrier** @@rule:arcane_barrier_ability@@
Arcane Barrier is a static ability. Arcane Barrier is written as "Arcane Barrier N" which means "If you would be dealt arcane damage, you may pay N\{r\} to prevent N of that damage."


### **Boost** @@rule:boost_ability@@
Boost is an optional additional-cost play-static ability that means "As an additional cost to play this, you may banish the top card of your deck. If you do, if it's a Mechanologist card, this gets go again."

#### If a player pays the additional cost to play a card with boost, the player is considered to have boosted and the played card is considered to have been boosted, even if the banished card is not a Mechanologist card.

#### A player cannot boost if they cannot pay the additional cost of banishing the top card of their deck.


### **Temper** @@rule:temper_ability@@
Temper is a triggered-static ability that means "When the combat chain closes, if this defended, put a -1\{d\} counter on it, then destroy it if it has zero \{d\}."


### **Blood Debt** @@rule:blood_debt_ability@@
Blood Debt is a triggered-static ability. Blood debt means "While this is in your banished zone, at the beginning of your end phase, lose 1\{h\}."

#### Blood debt only triggers if its source is public in the banished zone at the beginning of the owner's end phase.


### **Mentor** @@rule:mentor_ability@@

> **Note:** As of 2022, the mentor ability has been superseded by the Mentor type[[rule:mentor_type]]


### **Phantasm** @@rule:phantasm_ability@@
Phantasm is a triggered-static ability that means "Whenever this is defended by a non-Illusionist attack action card with 6 or more \{p\}, destroy this."

#### If an attack with Phantasm is being defended by a non-Illusionist attack action card that has the power property with a value of 6 or more, then the state-condition is met and a triggered-layer is put on the stack. When the triggered-layer resolves, if the trigger's event-condition is still met, the attack is destroyed.

#### If an attack is destroyed by phantasm before its chain link has resolved, the combat chain closes[[rule:closing_the_combat_chain]]. If an attack is destroyed by phantasm after its chain link has resolved, the combat chain does not close.


### **Spectra** @@rule:spectra_ability@@
Spectra is a static ability and a triggered-static ability that respectively mean "this can be attacked" and  "When this becomes the target of an attack, destroy this and close the combat chain."

#### An object with Spectra can be the target of an attack, even if it is not a living object.[[rule:attackable_target]]

#### When an object with Spectra becomes the target of an attack, a triggered-layer is put on the stack. When the triggered-layer resolves, the combat chain closes.[[rule:closing_the_combat_chain]]


### **Spellvoid** @@rule:spellvoid_ability@@
Spellvoid is a static ability. Spellvoid is written as "Spellvoid N" which means "If you would be dealt arcane damage, you may destroy this to prevent N of that damage."

#### If the controlling player cannot destroy the object with Spellvoid, they cannot apply the optional prevention effect.


### **Essence** @@rule:essence_ability@@
Essence is a meta-static ability. Essence is written in the format "Essence of [SUPERTYPES]" which means "You may have [SUPERTYPES] cards in your deck, as though your hero had those supertypes," where SUPERTYPES is a list of one or more supertypes.[[sec:supertypes]]


### **Fusion** @@rule:fusion_ability@@
Fusion is an optional additional-cost play-static ability. Fusion is written as "[SUPERTYPES] Fusion" which means "As an additional cost to play this, you may reveal (a/an) [SUPERTYPES] card(s) from your hand," where SUPERTYPES is a list of one or more supertypes.[[sec:supertypes]]

#### If a player pays the additional cost to play a card with fusion, the player is considered to have fused those supertypes and the played card is considered to have been fused.

#### A player cannot fuse if they cannot pay the additional cost of revealing the card(s) with the specified supertypes from their hand.

#### A player may only reveal up to one card for each of the supertypes listed. A single card may be revealed for one or more different supertypes.

#### If the list specifies "and," the player must reveal cards with all of the supertypes in the list. If the list specifies "and/or," the player must reveal cards with at least one of the supertypes on the list.


### **Heave** @@rule:heave_ability@@
Heave is a hidden triggered ability. Heave is written as "Heave N" which means "While this is in your hand and you have an empty arsenal zone, at the beginning of your end phase, you may pay N\{r\} and put this face-up into your arsenal. If you do, create N Seismic Surge tokens."

#### If a player pays the cost to pay the resource point cost and put the card with Heave face-up into their arsenal, the player is considered to have heaved and the card is considered to have been heaved.

#### A player cannot heave if they cannot pay the resource point cost or put the card with Heave face-up into their arsenal.


### **Quell** @@rule:quell_ability@@
Quell is a static ability. Quell is written as "Quell N" which means "If you would be dealt damage, you may pay N\{r\} to prevent N of that damage. If you do, destroy this at the beginning of the end phase."


### **Ward** @@rule:ward_ability@@
Ward is a static ability. Ward is written as "Ward N" which means "If you would be dealt damage, destroy this to prevent N of that damage."


### **Ephemeral** @@rule:ephemeral_ability@@
Ephemeral is a meta-static ability and a static ability that respectively mean "You can't start the game with this in your deck." and "If this would be put into a graveyard from anywhere, instead it ceases to exist."

#### A player cannot include a card with Ephemeral in their card-pool.[[rule:player_card_pool]]

#### A card that ceases to exist from Ephemeral is removed from the game. A card that is removed from the game has no further interaction with the rules and effects in the game.


### **Overpower** @@rule:overpower_ability@@
Overpower is a static ability that means "This can't be defended by more than one action card."

#### If an attack with overpower is currently defended by an action card, an additional action card cannot be added as a defending card to the attack's chain link.[[rule:add_defend_effect]].

#### If an attack is defended by two or more action cards and then the attack gains overpower, no cards are retroactively removed from defending.


### **Piercing** @@rule:piercing_ability@@
Piercing is a static ability. Piercing is written as "Piercing N" which means "If this is defended by an equipment, it gets +N\{p\}."


### **Stealth** @@rule:stealth_ability@@
<span style='color: rgba(0, 0, 0, 0);'>Stealth is an ability that means nothing.</span>


### **Mirage** @@rule:mirage_ability@@
Mirage is a static ability that means "When this is defending a non-Illusionist attack with 6 or more \{p\}, destroy this."


### **Pairs [with OBJECT]** @@rule:pairs_ability@@
Pairs is a static ability that means "Equip this only with an OBJECT.", where OBJECT is 1 or more object identities.

#### A card with pairs can only be equipped to a zone owned by a player if the player already has an OBJECT equipped, or if an OBJECT is being equipped as part of the same event.


### **Rune Gate** @@rule:rune_gate_ability@@
Rune Gate is a play-static ability that means "If you control Runechants equal to or greater than this's \{r\} cost, you may play it from your banished zone without paying its \{r\} cost."

#### If a player plays a card from their banished zone using rune gate, they are considered to have rune gated, and the card is considered to be rune gated.


### **Ambush** @@rule:ambush_ability@@
Ambush is a while-static ability that means "While this is in your arsenal, you may defend with it."


### **Crank** @@rule:crank_ability@@
Crank is a static ability that means "As this enters the arena, you may remove a steam counter from it. If you do, gain an action point."

#### If a player removes a steam counter using crank, they are considered to have cranked, and the card is considered to be cranked.


### **Modular** @@rule:modular_ability@@
Modular is a static ability that means "This may be equipped to any of your equipment zones. It has the subtype of the zone it's equipped to."

#### The equipment zones are Arms, Chest, Head, and Legs.

#### A card can only be equipped to its owner's equipment zones with Modular.

#### A card with modular does not have any of the equipment subtypes until it is equipped to a zone.


### **Protect** @@rule:protect_ability@@
Protect is a static ability that means "You may defend any hero attacked by an opponent with this."

#### If a player defends with a card with protect, they and the card are considered to have protected.


### **Scrap** @@rule:scrap_ability@@
Scrap is a play-static ability that means "As an additional cost to play this, you may banish an item or equipment from your graveyard."

#### If a player pays the additional cost to play a card with scrap, the player is considered to have scrapped, and the banished card is considered to have been scrapped.

#### A player cannot scrap if they cannot pay the additional cost of banishing an item or equipment from their graveyard.


### **Beat Chest** @@rule:beat_chest_ability@@
Beat Chest is a play-static ability that means "As an additional cost to play this, you may discard a card with 6 or more \{p\}."

#### If a player pays the additional cost to play a card with beat chest, the player is considered to have beaten chest.

#### A player cannot beat chest if they cannot pay the additional cost of discarding a card with 6 or more \{p\}.


### **Guardwell** @@rule:guardwell_ability@@
Guardwell is a static ability that means "When the combat chain closes, if this defended, put -1\{d\} counters on it equal to its \{d\}."


### **Universal** @@rule:universal_ability@@
Universal is a while-static ability that means "While in any zone, it is the same class as your hero."


### **Cloaked** @@rule:cloaked_ability@@
Cloaked is a static ability that means "Equip this face-down."


### **Arcane Shelter** @@rule:arcane_shelter_ability@@
Arcane Shelter is a static ability. Arcane Shelter is written as "Arcane Shelter N" which means "If you would be dealt arcane damage, destroy this to prevent N of that damage."


### **Meld** @@rule:meld_ability@@
Meld is a static ability that means "You may pay twice the base cost of this to play both halves of this."

#### If a player chooses to pay the alternative cost to play a card with meld, the player is considered to have melded and the card is melded. The card remains melded until it ceases to exist.

#### Meld sets the asset-cost of a card before increases and decreases are applied. ([[rule:play_calculate_asset]])

#### A melded card has the properties of both of its sides on a split-card[[sec:split_cards]]: both names, and the combination of its abilities, supertypes, types, and subtypes. If melded card is not a split-card, it is unaffected by meld.



## Label Keywords @@sec:label_keywords@@


### **Combo** @@rule:combo_label@@
Combo is a label for a static ability typically written as "Combo - If [NAMES] was the last attack this combat chain, [EFFECTS]" where NAMES is a list of one or more names.[[sec:name]]


### **Crush** @@rule:crush_label@@
Crush is a label for a triggered-static ability typically written as "Crush - When this deals 4 or more damage, [EFFECTS]."

#### The Crush ability is conditional on an event that deals damage, not a hit-event.[[rule:hit]]


### **Reprise** @@rule:reprise_label@@
Reprise is a label for a resolution ability typically written as "Reprise - If the defending hero has defended with a card from their hand this chain link, [EFFECTS]."

#### The condition of a reprise ability effect is checked on resolution - it does not retroactively generate effects if the condition is met after resolution.


### **Channel** @@rule:channel_label@@
Channel is a label for an ability typically written as "Channel [SUPERTYPE] - At the beginning of your end phase, put a flow counter on this then destroy it unless you put a [SUPERTYPE] card from your pitch zone on the bottom of your deck for each flow counter on it." where SUPERTYPE is a supertype.[[sec:supertypes]]
%


### **Material** @@rule:material_label@@
Material is a label for an ability typically written as "Material - While this is under a permanent, [EFFECTS]."


### **Rupture** @@rule:rupture_label@@
Rupture is a label for an ability typically written as "Rupture - If this is played [as / at] chain link 4 or higher, [EFFECTS]."
%


### **Contract** @@rule:contract_label@@
Contract is a label for a static ability typically written as "Contract - You are contracted to [CONDITION]. Whenever you complete this contract, [EFFECT]" where CONDITION is one or more contract conditions, and EFFECT the reward for completing the contract.[[rule:contract_effect]]


### **Surge** @@rule:surge_label@@
Surge is a label for a resolution or static ability typically written as "Surge - If this deals N damage, [EFFECTS]."


### **Solflare** @@rule:solflare_label@@
Solflare is a label for an ability typically written as "Solflare - When this is charged to your hero's soul, [EFFECTS]."


### **Unity** @@rule:unity_label@@
Unity is a label for an ability typically written as "Unity - When this defends together with a card from hand, [EFFECTS]."


### **Evo Upgrade** @@rule:evo_upgrade_label@@
Evo Upgrade is a label for an ability typically written as "Evo Upgrade - [EFFECTS] for each evo you have equipped" or "Evo Upgrade - [EFFECTS] where X is the number of evos you have equipped."


### **Galvanize** @@rule:galvanize_label@@
Galvanize is a label for an ability typically written as "Galvanize - When this defends, you may destroy an item you control. If you do, [EFFECTS]"


### **Tower** @@rule:tower_label@@
Tower is a label for an ability typically written as "Tower - If this has 13 or more \{p\}, [EFFECTS]"


### **Decompose** @@rule:decompose_label@@
Decompose is a label for an ability typically written as "Decompose - You may banish 2 Earth cards and an action card from your graveyard. If you do, [EFFECTS]."


### **Earth Bond** @@rule:earth_bond_label@@
Earth Bond is a label for an ability typically written as "Earth Bond - If an earth card was pitched to play this, [EFFECTS]."


### **Lightning Flow** @@rule:lightning_flow_label@@
Lightning Flow is a label for an ability typically written as "Lightning Flow - If you've played a Lightning card this turn, [EFFECTS]."


### **Heavy** @@rule:heavy_label@@
Heavy is a label for an ability typically written as "Heavy - If this is the only card equipped to your weapon zones, [EFFECTS]."



## Effect Keywords @@sec:effect_keywords@@


### **Banish** @@rule:banish_effect@@
Banish is a discrete effect. To banish an object, the instructed player moves the object to its owner's banished zone.

#### Putting an object into the banished zone because of a rule or effect other than banish is not considered banishing that object.

#### If an object would be banished but a replacement effect specifically modifies the destination to a zone other than the banished zone, the card is still considered banished.

#### If an object is banished until a certain condition is met, the banish event is generated normally and the object is returned to its previous zone immediately after the condition is met as a delayed discrete effect. If the object ceases to exist before being returned, the return fails.


### **Create (token)** @@rule:create_token_effect@@
Create is a discrete effect. To create a token, produce the specified token in the arena.

#### The properties of a created token, specified by the token keyword, are defined in [[sec:token_keywords]].

#### A token enters the arena as it is created. Effects that trigger from the token entering the arena trigger as though the token was created first, then entered the arena. If an effect applies to the created token as it is created, it applies to it as it enters the arena.

#### A token enters the arena under the control of the player instructed to create it. If the token is created in a zone owned by a player, the token enters that zone under the control of that player.


### **Deal (damage)** @@rule:damage_effect@@
Deal is a discrete effect. To deal damage to an object, that object loses \{h\} equal to the damage dealt.

#### If an object loses life from being dealt damage, the ability that generated the damage effect and the ability's source of the damage are considered to have dealt that damage. If the effect specifies the source of the damage, that source is considered to have dealt that damage instead. If the source is a non-living card, the player that controls the source and the player's hero are also considered to have dealt that damage.

#### @@rule:damage_types@@ There are 3 types of damage: generic, physical, and arcane. Generic damage is damage without a specified type - it is referred to as "damage." Physical damage is damage dealt by an object using its power value \{p\} during the damage step of combat - it is referred to as "\{p\} damage"[[sec:damage_step]]. Arcane damage is damage dealt by an effect that specifically deals arcane damage.

#### If a non-living object would be dealt damage, the effect fails.[[rule:living_object]]

#### Losing life because of a rule or effect other than dealing damage is not considered dealing damage. An effect that causes life loss is not considered damage.[[rule:lose_asset_effect]]

#### An effect that triggers from a specific type of damage being dealt, other than generic damage, does not trigger from another type of damage being dealt.

#### An effect that modifies or prevents a specific type of damage,  other than generic damage, cannot modify or prevent another type of damage.


### **Destroy** @@rule:destroy_effect@@
Destroy is a discrete effect. To destroy an object, put it into its owner's graveyard.

#### Putting an object into the graveyard because of a rule or effect other than destroy is not considered destroying that object.


### **Discard** @@rule:discard_effect@@
Discard is a discrete effect. To discard a card from a player's hand, put it from the player's hand into their graveyard.

#### Putting an object into the graveyard because of a rule or effect other than discard is not considered discarding that object.

#### If a player tries to discard a card when there are no cards in their hand, the discard effect fails.

#### If a card is discarded but a replacement effect modifies the destination to a zone other than the graveyard, the card is still considered discarded.


### **Draw** @@rule:draw_effect@@
Draw is a discrete effect. To draw a card, move the top card of the deck to the player's hand.

#### Putting an card into the hand because of a rule or effect other than draw is not considered drawing that card.

#### If a player tries to draw a card when there are no cards in their deck, the draw effect fails.

#### If a card is drawn but a replacement effect modifies the destination to a zone other than the hand, the card is still considered drawn.


### **Gain (asset)** @@rule:gain_asset_effect@@
Gain is a discrete effect. To gain an asset, the player's or object's assets of the given type is increased by the specified amount.[[sec:assets]]

#### If a living object gains \{h\}, its life total is increased by the specified amount. If the object does not have the life property, then the gain effect fails.

#### If a non-turn player would gain action points, then the gain effect fails.


### **Gets (numerical property)** @@rule:gets_numeric_effect@@
Gets is a continuous effect, referred to as modify, and includes all modifications to existing numerical properties. To modify an object, the numerical properties of the object are altered by the specified amount.[[rule:numeric_property]]

> **Note:** From Cards printed before 2023 have also used the keyword "gains/gain" and "has/have."

#### If the effect specifies to alter an existing property of the object, but the object does not have that property, it does not give it that property.

#### If the effect specifies the object has a base numerical property, the object gains that property with the specified base value. If the object already has that numeric property, it sets the base value of that property.


### **Gets / Is (non-numerical property)** @@rule:gets_property_effect@@
Gets/is is a continuous effect, referred to as modify. To modify an object, the object gains the specified object properties.[[cha:object_properties]]

> **Note:** From Cards printed before 2023 have also used the keyword "gains/gain" and "has/have."

#### If the effect specifies the object gains a property, the object gains that property in addition to any existing properties it already has.


### **Intimidate** @@rule:intimidate_effect@@
Intimidate is a discrete effect and delayed-triggered effect. To intimidate a player, they banish a card from their hand face-down, and then at the beginning of the end phase, it returns it to their hand.

#### The player is considered to have been intimidated, even if they did not banish a card from their hand.

#### If a player is not specified, the intimidate is a targeted effect.[[rule:targets]]

#### The triggered effect only returns the cards banished by its ability. If there are two or more temporary-triggered effects created by separate intimidate effects, they each only return the cards banished by their respective intimidate effect.


### **Look** @@rule:look_effect@@
Look is a discrete effect or continuous effect. To look at a private object, the information about the properties of that object becomes known to the specified player(s).

#### If a duration is not specified, look is a discrete effect and the player(s) may look at the specified object until the next event in the game occurs. If a duration is specified, look is a continuous effect and the player(s) may look at the specified object for the duration as if it were a private object they owned that is not in a deck.[[rule:object_visibility]].

#### If a player looks at a private object, it does not become a public object and it is not put into another zone.

#### If the object is public, the look effect fails.

#### If look is a continuous effect and the object is specified by a location, the object the player may look at are determined as a game state action. If the object a player may look at changes due to a rule or effect, the player may not look at that new object until any player would gain priority.


### **Lose (asset)**
Lose is a discrete effect. To lose an asset, the player's or object's assets of the given type is decreased by the specified amo nt.[[sec:assets]] @@rule:lose_asset_effect@@

#### If a living object lose \{h\}, its life total is decreased by the specified amount. If the object does not have the life property, then the lose effect fails.

#### Losing life is not considered as damage being dealt, unless it is the result of a damage effect[[rule:damage_effect]]. Losing life is not considered as a hit, unless it is the result of damage being dealt by an attack during the damage step of combat[[rule:hit]]


### **Loses (non-numerical property)** @@rule:lose_property_effect@@
Loses is a continuous effect, referred to as modify. To modify an object, the object loses the specified object base properties.[[cha:object_properties]]

#### If the effect specifies the object loses a property, and the object does not have that property as a base property, it does not lose that property.


### **Put (counter)** @@rule:put_counter_effect@@
Put/Return is a discrete effect. To put a counter onto an object, a specified counter begins to exist on the object.


### **Put / Return (object)** @@rule:put_object_effect@@
Put/Return is a discrete effect. To put/return an object into/to a zone, move it from its current zone to the specified zone.


### **Remove (counter)** @@rule:remove_counter_effect@@
Remove is a discrete effect. To remove a counter from an object, a specified counter ceases to exist on the object.

#### If there are two or more of the same counters on an object, it is irrelevant which of those counters is removed.

#### If two or more counters are removed, they are removed simultaneously in a single event.


### **Reveal** @@rule:reveal_effect@@
Reveal is a discrete effect or continuous effect. To reveal a private object, make it public, then make it private again.[[rule:object_visibility]]

#### Making an object public because of a rule or effect other than reveal is not considered revealing that object.

#### If a duration is not specified, reveal is a discrete effect and the object becomes public and then private as consecutive events. If a duration is specified, reveal is a continuous effect and the object remains public for the duration, then it becomes private.

#### Revealing a private object does not change its position in the deck (if it's in the deck) or put it into another zone.

#### If the object is public, the reveal effect fails.

#### If a player is instructed to reveal cards until a condition is met, it is considered to be revealing N cards as a single reveal event, where N is the total number of cards revealed this way. If there are no more cards to reveal and the specified condition is not met, the effect is considered to have failed - effects that trigger from revealing are still triggered.


### **Roll** @@rule:roll_effect@@
Roll is a discrete effect. To roll a die, toss a die to produce a sufficiently random orientation, and then the value of the uppermost die face is used as the result of the roll.

#### A roll is specified with the number and type of dice to roll. If two or more dice are specified then all dice are rolled and their result is taken simultaneously.

#### A die used in a roll must have uniquely distinguishable faces, with each face representative of a distinct integer value from one up to, and including, the number of faces on the die; and an equal likelihood that it will land face up.


### **Search** @@rule:search_effect@@
Search is a discrete effect. To search for a card in a set of zones, the player looks at all the cards in those zones and then chooses a card from them.

#### If the search specifies any properties of the card that can be chosen, the search is performed on a non-empty zone, and there are no public cards with those properties in that zone; the player may choose to fail the search, even if there is a private card with those properties in that zone.

#### If the search specifies any properties of the card that can be chosen and there are one or more public cards with those properties in that zone, the player cannot fail the search.

#### If the search does not specify any properties of the card that can be chosen and the search is performed on a non-empty zone, the player cannot fail the search.

#### If the zone is empty, the search effect fails.


### **Shuffle** @@rule:shuffle_effect@@
Shuffle is a discrete effect. To shuffle a zone, put the cards in that zone in a sufficiently random order such that no one knows their order.

#### If there are no cards in the zone to shuffle, the zone is still considered shuffled.

#### If the effect specifies to shuffle cards into a zone, put the cards into the zone then shuffle that zone.

#### If the effect does not specify what zone to shuffle, the player shuffles their own deck.


### **Name** @@rule:name_effect@@
Name is a discrete effect. To name an object, declare the name property of an object.[[sec:name]]

#### An object cannot be named using its moniker, the full name of the object must be declared.

#### Only specified objects that exist and are legal in the game can be named. The player cannot name an object if it does not meet the specifications of the effect, or if the name does not exist on an object that is legal for the game.


### **Opt** @@rule:opt_effect@@
Opt is a discrete effect. To opt N, the player looks at the top N cards of their deck, then puts any number of those cards on the top or bottom of their deck in any order.

#### If the deck has less than N cards, the player will look at all cards in their deck and put them back in any order.

#### If the deck has no cards in it, the opt effect fails.


### **Reload** @@rule:reload_effect@@
Reload is an optional discrete effect. To reload a card, if the player's arsenal is empty and they choose to do so, move it from the player's hand to their arsenal face-down.

#### If the player has two or more arsenal zones, all of those arsenal zones must be empty for the player's arsenal to be considered empty.


### **Turn** @@rule:turn_effect@@
Turn is a discrete effect. To turn a card face-up or face-down, that card becomes public (face-up) or private (face-down) respectively.[[rule:object_visibility]]

#### If the card already has the specified visibility, the turn effect fails.


### **Become / Copy** @@rule:copy_effect@@
Become/Copy is a continuous effect. To become/copy a reference, the object loses all existing properties and gets all of the copyable properties of the specified reference.

#### The copyable properties of a card are determined by the printed properties on that card - properties that are derived from printed properties (abilities, type, supertypes, subtypes) are not duplicated (doubled up) on the object. The copyable properties of a token are determined by the properties that token was created with.

#### If the reference has any determined parameters from when it was played, activated, or otherwise created, the object also uses those parameters.

#### After the become/copy effect has occurred, any change to the copyable values of the reference will not change the copied values of the subject.

#### If an object has become the reference, any other effect that would cause the object to become the same reference fails.


### **Negate** @@rule:negate_effect@@
Negate is a discrete effect. To negate a layer, the layer is cleared from the stack and it does not resolve.

#### If a layer negates itself while resolving, it does not finish resolving.


### **Repeat** @@rule:repeat_effect@@
Repeat is a discrete effect. To repeat a process, perform the instructions of that process again.

#### If no process is specifically stated, the process to repeat refers to the discrete effects preceding the repeat effect in the same resolution ability.

#### If the instructions would be repeated indefinitely, the repeated process stops when the instructions fail to advance the game state.


### **Reroll** @@rule:reroll_effect@@
Reroll is a replacement effect. To reroll dice, those dice are rolled again and their result is taken as if it were the first time they were rolled.

#### If a die is rerolled its original result is considered to never have happened.

#### If an event is modified by two or more reroll effects, those reroll effects occur one by one in the order the event was modified.


### **Charge** @@rule:charge_effect@@
Charge is a discrete effect. To charge a card, move it from the player's hand to their hero's soul.

#### The player that controls the effect is considered to have charged a card, and the card put into their soul is considered to be charged.

#### Moving a card to a hero's soul from a rule or effect other than charge is not considered charging.


### **Distribute** @@rule:distribute_effect@@
Distribute is a discrete effect. To distribute counters, create the counters if they do not exist, and divide and put them on a specified set of objects.


### **Pay** @@rule:pay_effect@@
Pay is a discrete effect. To pay an asset-cost, the player spends assets of the specified type and amount.[[rule:asset_cost]]

#### Pay effects are optional and the affected player can refuse to pay the asset-cost.


### **Add (defend)** @@rule:add_defend_effect@@
Add is a discrete effect. To add a card to a chain link as a defending card, move it from its current zone onto that chain link as a defending card.[[rule:defending_card]]


### **Ignore** @@rule:ignore_effect@@
Ignore is a replacement effect. To ignore an event or part of an event, after it has been completed, it is considered to never have happened.

#### If an effect is conditional or dependent on the result of an event that is ignored, the ignored part of the event is not considered to have happened.

#### If there are two or more identical parts of an event and the ignore effect does not specify all of those parts, only the specified parts are ignored.

#### If an event is modified by both a reroll and ignore effect, the reroll occurs before its results are ignored.


### **Freeze** @@rule:freeze_effect@@
Freeze is a continuous effect. To freeze an object, that object cannot be played and its abilities cannot be activated for the duration of the effect.

#### The player that controls the effect is considered to have frozen an object, and the object is considered to be frozen. The object can be unfrozen by an effect.[[rule:unfreeze_effect]]

#### If no duration is specified, the player freezes the object until the start of their next turn.

#### If a freeze effect already applies to an object, a new freeze effect that would apply to that object does not fail.


### **Gain (control)** @@rule:gain_control_effect@@
Gain is a continuous effect. To gain control of an object, that player is considered to control the object instead of its previous controller.


### **Transform** @@rule:transform_effect@@
Transform is a discrete effect. To transform an object into a permanent, put the object under the permanent.[[rule:under_definition]]

#### The object(s) that are put under the permanent are considered to have transformed into the permanent. The permanent is considered to have transformed from the object(s).

#### If the specified object to transform into exists but is not a permanent, it first becomes permanent, and then the object is put under it.

#### If the specified permanent is a token keyword, create that token, then put the transformed objects under it.[[sec:token_keywords]]

#### If the transform involves transforming two or more objects into a permanent, all of those objects must exist and be put under the permanent, otherwise the effect fails and no objects are transformed.


### **Unfreeze** @@rule:unfreeze_effect@@
Unfreeze is a discrete effect. To unfreeze an object, all existing freeze effects no longer apply to that object.[[rule:freeze_effect]]

#### If an object is unfrozen, all existing freeze effects that apply to an object cease to exist. After the unfreeze event has occurred, the object may be frozen again by new freeze effects.

#### If unfreeze applies to an object that is not frozen, the effect fails.


### **Attack** @@rule:attack_effect@@
Attack is a targeted discrete effect. To attack a target with an object, the object becomes an attack and chain link on the combat chain.

#### A layer on the stack that can generate the attack effect is an attack-layer.[[rule:attack_layer]].

#### When an attack-layer resolves on the stack, the specified object becomes an attack and chain link on the combat chain and effects that applied to the attack-layer apply to the object as an attack instead[[rule:attack_step_attack_layer]]. If the object does not exist or cannot become an attack, the combat chain closes instead[[rule:illegal_attack_source]].

#### If an attack-layer is added to the stack, the combat chain opens (if it is closed) and the Layer Step of combat begins.[[sec:layer_step]]

#### To add an attack-layer onto the stack, a legal attackable target must be declared as the target of the attack.[[rule:attackable_target]]


### **Contract** @@rule:contract_effect@@
Contract is a continuous effect. To contract a player, the player is given a specified set of actions to complete.

#### The contract starts when the contract effect is first generated and ends when the effect ceases to exist. A player is considered to have completed a contract if they have performed the actions specified by the contract while the effect exists. If another player performs the actions specified by the contract, they are not considered to have completed the contract because they are not the player that is contracted.

#### A contract can be completed any number of times while the effect exists.


### **Create (card)** @@rule:create_card_effect@@
Create is a discrete effect. To create a card in a zone, produce the specified card in that zone.

#### The properties of a created card, specified by name (and pitch if any), are defined by the properties printed on that card.

#### A card that is created does not exist before being created. The created card does not have to be included in a player's card-pool to be created.


### **Equip** @@rule:equip_effect@@
Equip is a discrete effect. To equip an object, put the object into an equipment or weapon zone as a permanent and it becomes equipped to that zone.

#### If no zone is specified, the object may be equipped to any zone determined by its subtype.[[cha:zones]][[sec:subtypes]]

#### An object can only be equipped if it has one of the following subtypes: 1H, 2H, Arms, Chest, Heads, Legs, Off-Hand, or Quiver.

#### An object can only be equipped to a zone if the zone is empty and it is not already equipped to a zone of the same type. If a rule or effect requires an object to be equipped to two or more zones, all of those zones must be empty.

#### If the specified object is a token keyword[[sec:token_keywords]], create that token, then equip it. If the token cannot be created or equipped, the effect fails.

#### If an object cannot be equipped, it does not become a permanent.

#### If an equipped object ceases to exist, it is no longer equipped to any zones.


### **Move (counter)** @@rule:move_effect@@
Move is a discrete effect. To move a counter, remove the counter from its current object and put it onto the specified object.[[rule:put_counter_effect]][[rule:remove_counter_effect]]

#### If no specified counter exists or can be moved, no counters are removed from any object or put onto the specified object.


### **Awaken** @@rule:awaken_effect@@
Awaken is a discrete effect. To awaken a double-faced card, its back face becomes its active face.[[sec:double_faced_cards]]

#### If an object is not a double-sided card, its back face is already active, or its back face can otherwise not be made active, the awaken effect fails.


### **Pitch** @@rule:pitch_effect@@
Pitch is a discrete effect. To pitch a card, put it from the player's hand into their pitch zone and that player gains resources equal to its pitch value.[[rule:pitching]]

#### If the effect instructs the player to pitch two or more cards, all of those cards must exist and be pitched, otherwise the pitch effect fails.


### **Clash** @@rule:clash_effect@@
Clash is a discrete effect. To clash, the clashing players reveal the top card of their respective decks, and then the player that reveals the card with the greatest \{p\} value wins the clash.

#### The \{p\} values of the revealed cards are compared and the player that revealed the card with the greatest \{p\} value is considered to have won the clash by revealing that card.

#### If a player's revealed card does not have the power property, or they do not reveal a card, any other revealed card with the power property is considered to have greater power[[rule:property_exists]].

#### If none of the players reveals a card with power greater than all other revealed cards, no player is considered to have won the clash.

#### If the heroes specified by the clash do not exist or there are less than two clashing heroes, the clash effect fails.


### **Wager** @@rule:wager_effect@@
Wager is a continuous effect. To wager a prize with another player, when the chain link of the attack resolves, if the attack has hit, the controller wins the prize, otherwise the other player wins the prize.

#### After the effect is generated, the attack of the wager and the player that controls the effect are considered to have wagered. When the trigger of a wager effect resolves and the attack has hit, that attack and the player that controls the effect are considered to have won the wager, otherwise the other player is considered to have won the wager.

#### If the prize is a token, the player that wins creates that token under their control. If there is no prize specified by the effect, the player is simply considered to have won the wager.


### **Amp** @@rule:amp_effect@@
Amp is a continuous effect. To amp N, the next time an event the player controls would deal arcane damage this turn, instead it deals that much arcane damage plus N.


### **Transcend** @@rule:transcend_effect@@
Transcend is a discrete effect. To transcend, the transcend source is put into its owner's hand with its back-face active.

#### The player that controls the effect is considered to have transcended.


### **Exchange** @@rule:exchange_effect@@
Exchange is a discrete effect. To exchange objects, the objects swap their respective zone, visibility, and control with each other.

#### The swap in zone, visibility, and control for both objects happens simultaneously as a move event. If either object cannot complete the move successfully, the effect fails.

#### If an object is equipped, the object it will be exchanged with will be equipped as part of the move event. If the object cannot be equipped, the effect fails.


### **Mark** @@rule:mark_effect@@
Mark is a discrete effect. To mark a hero, that hero has the marked condition[[sec:marked]].


### **Retrieve** @@rule:retrieve_effect@@
Retrieve is a discrete effect. To retrieve a card, the player may pay \{r\} to equip the card.

#### The card must exist and be able to be equipped for the player to pay \{r\}. If the player cannot equip the card, they cannot choose to pay \{r\}.


### **Return to the Brood** @@rule:return_to_the_brood_effect@@
Return to the Brood is a discrete effect. To return to the brood, existing become/copy effects that apply to the player's hero cease to exist.



## Token Keywords @@sec:token_keywords@@


### **Quicken** @@rule:quicken_token@@
A Quicken token is a token with the name "Quicken," the subtype aura, and the triggered-static ability "When you play an attack action card or activate a weapon attack, destroy this then the attack gains go again."


### **Seismic Surge** @@rule:seismic_surge_token@@
A Seismic Surge token is a token with the name "Seismic Surge," the subtype aura, and the triggered-static ability "At the beginning of your action phase, destroy this then the next Guardian attack action card you play this turn costs \{r\} less to play."


### **Runechant** @@rule:runechant_token@@
A Runechant token is a token with the name "Runechant," the subtype aura, and the triggered-static ability "When you play an attack action card or activate a weapon attack, destroy this and deal 1 arcane damage to target opposing hero."


### **Copper** @@rule:copper_token@@
A Copper token is a token with the name "Copper," the subtype item, and the activated ability "Action ‐- \{r\}\{r\}\{r\}\{r\}, destroy this: Draw a card. Go again."


### **Zen State** @@rule:zen_state_token@@
A Zen State token is a token with the name "Zen State," the supertype ninja, the subtype aura, and the static abilities "This enters the arena with 1 balance counter on it. At the beginning of your action phase, destroy this unless you remove a balance counter from it." and "Whenever your hero would be dealt damage, prevent 1 damage that source would deal."


### **Blasmophet, the Soul Harvester** @@rule:blasmophet_token@@
A Blasmophet, the Soul Harvester token is a token with the name "Blasmophet, the Soul Harvester," the supertype shadow, the subtypes demon and ally, a power of 6\{p\}, a life of 6\{h\}, the activated ability "Once per Turn Action -- 0: Attack," and the triggered-static ability "Whenever Blasmophet attacks, you may banish a Shadow card from your hand. If you do, you may banish a card from the defending hero's soul."


### **Soul Shackle** @@rule:soul_shackle_token@@
A Soul Shackle token is a token with the name "Soul Shackle," the subtype aura, and the triggered-static ability "At the beginning of your action phase, banish the top card of your deck."


### **Spectral Shield** @@rule:spectral_shield_token@@
A Spectral Shield token is a token with the name "Spectral Shield," the supertype illusionist, the subtype aura, and the static ability "Ward 1."


### **Ursur, the Soul Reaper** @@rule:ursur_token@@
A Ursur, the Soul Reaper token is a token with the name "Ursur, the Soul Reaper," the supertype shadow, the subtypes demon and ally, a power of 6\{p\}, a life of 6\{h\}, the activated ability "Once per Turn Action -- 0: Attack," and the static ability "While Ursur is attacking a hero with 1 or more cards in their soul, the attack has go again."


### **Frostbite** @@rule:frostbite_token@@
A Frostbite token is a token with the name "Frostbite," the supertype elemental, the subtype aura, the static ability "Cards and abilities cost you an additional \{r\} to play or activate." and the triggered-static ability "At the beginning of your end phase or when you play a card or activate an ability, destroy this."


### **Embodiment of Earth** @@rule:embodiment_of_earth_token@@
An Embodiment of Earth token is a token with the name "Embodiment of Earth," the supertype elemental, the subtype aura, the static ability "'Non-attack' action cards you control have +1\{d\} while defending." and the triggered-static ability "At the beginning of your action phase, destroy this."


### **Embodiment of Lightning** @@rule:embodiment_of_lightning_token@@
An Embodiment of Lightning token is a token with the name "Embodiment of Lightning," the supertype elemental, the subtype aura, and the triggered-static ability "When you play an attack action card, destroy this and the attack gains go again."


### **Silver** @@rule:silver_token@@
A Silver token is a token with the name "Silver," the subtype item, and the activated ability "Action ‐- \{r\}\{r\}\{r\}, destroy this: Draw a card. Go again."


### **Ash** @@rule:ash_token@@
An Ash token is a token with the name "Ash," the supertypes draconic and illusionist, the subtype ash, and the static ability "Material - While this is under a permanent, that object has phantasm."


### **Aether Ashwing** @@rule:aether_ashwing_token@@
An Aether Ashwing token is a token with the name "Aether Ashwing," the supertypes draconic and illusionist, the subtypes dragon and ally, a power of 1\{p\}, a life of 1\{h\}, and the static ability "Arcane Barrier 1."


### **Gold** @@rule:gold_token@@
A Gold token is a token with the name "Gold," the subtype item, and the activated ability "Action ‐-\{r\}\{r\}, destroy this: Draw a card. Go again."


### **Ponder** @@rule:ponder_token@@
A Ponder token is a token with the name "Ponder," the subtype aura, and the triggered ability "At the beginning of your end phase, destroy this and draw a card."


### **Spellbane Aegis** @@rule:spellbane_ageis_token@@
A Spellbane Aegis token is a token with the name "Spellbane Aegis," the subtype aura, and the static ability "Spellvoid 1."


### **Bloodrot Pox** @@rule:bloodrot_pox_token@@
A Bloodrot Pox token is a token with the name "Bloodrot Pox," the subtype aura, and the triggered ability "At the beginning of your end phase, destroy this, then it deals 2 damage to you unless you pay \{r\}\{r\}\{r\}."


### **Frailty** @@rule:frailty_token@@
A Frailty token is a token with the name "Frailty," the subtype aura, the static ability "Your attack action cards played from arsenal and weapon attacks have -1\{p\}," and the triggered ability "At the beginning of your end phase, destroy this."


### **Inertia** @@rule:inertia_token@@
A Inertia token is a token with the name "Inertia," the subtype aura, and the triggered ability "At the beginning of your end phase, destroy this, then put all cards from your hand and arsenal on the bottom of your deck."


### **Courage** @@rule:courage_token@@
A Courage token is a token with the name "Courage," the subtype aura, and the triggered ability "When you play an attack action card or activate a weapon attack, destroy this and the attack gets +1\{p\}."


### **Eloquence** @@rule:eloquence_token@@
An Eloquence token is a token with the name "Eloquence," the subtype aura, and the triggered ability "When you play a non-attack action card, destroy this and the card gets go again."


### **Nasreth, the Soul Harrower** @@rule:nasreth_token@@
A Nasreth, the Soul Harrower token is a token with the name "Nasreth, the Soul Harrower," the supertype shadow, the subtypes demon and ally, a power of 6\{p\}, a life of 6\{h\}, the activated ability "Once per Turn Action -- 0: Attack," and the static ability "When Nasreth hits a hero, banish a card from their soul. If a Light card is banished this way, gain 1\{h\}."


### **Hyper Driver** @@rule:hyper_driver_token@@
A Hyper Driver token is a token with the name "Hyper Driver," the subtype item, the triggered ability "When this has no steam counters, destroy it," and the triggered ability "Once per turn, when you boost a card, remove a steam counter from this and gain \{r\}."


### **Might** @@rule:might_token@@
A Might token is a token with the name "Might," the subtype aura, and the triggered ability "At the start of your turn, destroy this, then your next attack this turn gets +1\{p\}."


### **Vigor** @@rule:vigor_token@@
A Vigor token is a token with the name "Vigor," the subtype aura, and the triggered ability "At the start of your turn, destroy this, then gain \{r\}."


### **Agility** @@rule:agility_token@@
An Agility token is a token with the name "Agility," the subtype aura, and the triggered ability "At the start of your turn, destroy this, then your next attack this turn gets go again."


### **Cintari Sellsword** @@rule:cintari_sellsword_token@@
A Cintari Sellsword token is a token with the name "Cintari Sellsword," the supertype warrior, the subtypes mercenary and ally, a power of 3\{p\}, a life of 2\{h\}, the activated ability "Once per Turn Action -- \{r\}: Attack. Go again," and the static ability "Cintari Sellsword can only attack if you've attacked with a weapon this turn."


### **Graphene Chelicera** @@rule:graphene_chelicera_token@@
A Graphene Chelicera token is a token with the name "Graphene Chelicera," the supertype Assassin, the type Weapon, the subtypes Dagger and (1H), a power of 1\{p\}, the activated ability "Once per Turn Action -- \{r\}: Attack," and the triggered ability "When this attacks a marked hero, the attack gets go again."


### **Fealty** @@rule:fealty_token@@
A Fealty token is a token with the name "Fealty," the supertype Draconic, the subtype aura, and the activated ability "Instant -- Destroy this: The next card you play this turn is Draconic. At the beginning of your end phase, if you haven't created a Fealty token or played a Draconic card this turn, destroy this."
