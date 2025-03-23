[REF book=CR chap=7]

# Combat @@cha:combat@@



## General @@sec:combat_general@@


### Combat is a game state where the combat chain is open and attacks undergo resolution in steps on the stack and combat chain. The resolution of a chain link consists of seven steps in order: Layer, Attack, Defend, Reaction, Damage, and Resolution.

#### @@rule:actions_during_combat@@ During combat, while the combat chain is open, a player cannot play cards or activate activated abilities with the type action, except for attacks during the Resolution Step of combat[[sec:resolution_step]]. An action card/ability can still be played/activated as an instant during any step of combat when a player has priority.


### @@rule:combat_chain@@ The combat chain is a zone[[sec:combat_chain_zone]] that is open during combat and closed otherwise. It comprises chain links when it is open, and is empty when it is closed.

#### The combat chain starts the game closed. If the combat chain is closed and an attack is added to the stack, the combat chain opens and the Layer Step begins immediately. The combat chain remains open until it is closed again[[rule:closing_the_combat_chain]].

#### When referring to combat chain as a time, the combat chain starts when it opens and ends when closes. If an effect states "this combat chain" it refers to the current combat chain if it is open - if the combat chain is closed the effect fails to be generated.


### @@rule:chain_link@@ A chain link is an element of the combat chain and represents the resolution of an attack. A chain link is neither an object nor a zone. A chain link comprises an active-attack, an attack-source (if any), and any number of defending cards.

#### @@rule:create_chain_link@@ A chain link is created when an attack is added to the combat chain as a chain link[[rule:becomes_chain_link]]. The attack becomes the active-attack of chain link N+1, where N is the number of existing chain links on the combat chain.

#### @@rule:active_chain_link@@ The active chain link is the most recent chain link of the combat chain. When chain link N+1 is created, chain link N (if any) becomes the previous chain link and chain link N+1 becomes the active chain link, until the combat chain closes.

#### @@rule:chain_link_last_known_info@@ When referring to a chain link as a collection, the properties, control, and ownership of a chain link are considered to be the same as the active-attack of that chain link. If the active-attack of a chain link ceases to exist, last known information about the active-attack is used to determine the properties, control, and ownership.[[rule:last_known_information]]

> **Example:** Double Strike has the text "When this chain link resolves, banish this." Even if the Double Strike ceases to exist, the chain link remains, and is considered a Ninja chain link controlled by the attacking hero.

#### When referring to a chain link as a time, a chain link starts when it becomes the active chain link and ends when it is no longer the active chain link or the combat chain closes. If an effect states "this chain link" it refers to the active chain link - if there is no active chain link (the combat chain is closed) the effect fails to be generated.

#### When a layer is added to the stack while the combat chain is open, it is considered to be played/activated/triggered on the active chain link (if any), for rules and effects[[rule:active_chain_link]]. If there is no active chain link on the combat chain, it is not considered to be played/activated/triggered on any chain link.

#### To put a card on a chain link, that card moves to the combat chain and is associated with that chain link until it leaves the combat chain. Cards on a chain link are considered to be on the combat chain and in the arena.


### @@rule:active_attack@@ An active-attack, is an attack that has been put onto the combat chain as a chain link[[sec:attacks]][[rule:create_chain_link]].

#### If a card is put onto a chain link as an attacking card, the existing active-attack (if any) is cleared, and the new card becomes the active-attack for that chain link. It is considered a new attack, but the attack target(s) remain the same.

> **Example:** Uzuri has the text "[...] put target attacking card with stealth from the active chain link on the bottom of its owner's deck, then put the banished card onto the active chain link as the attacking card." The card with stealth is essentially replaced by the banished card as the attack on the chain link. The banished card is considered a new attack for rules and effects, except that the target of the attack stays the same.


### @@rule:defending_card@@ A defending card is a card that is designated as defending on a chain link for an attack-target by a rule or effect[[rule:declare_defense]][[rule:resolve_defence_reaction]][[rule:add_defend_effect]].

#### To be added as a defending card, the card is put on the respective chain link. The card is considered to be defending until it leaves the combat chain. Then the "defend" event occurs and effects that trigger from defending are triggered. The controller of the card at the time it defends is considered to have defended with that card.

> **Example:** Surging Militia has the text "This gets +1\{p\} for each non-equipment card defending it." and Inertia Trap has the text "When this defends an attack with \{p\} greater than its base, [...]" When Inertia Trap becomes a defending card against Surging Militia, the Surging Militia will gain +1\{p\} before the defend event occurs, and thus Inertia Trap will trigger.

#### If an effect would add a card on a chain link as a defending card, but the card is already defending on that chain link or the card cannot become a defending card due to another effect, the effect fails, no defend event occurs, and the card does not move zones.

> **Example:** Amulet of Havencall has the text "Defense Reaction -- Destroy this: Search your deck for a Rally the Rearguard, add it to this chain link as a defending card, then shuffle." If Rally the Rearguard cannot be added as a defending card, it remains in the deck and the deck is shuffled.

> **Example:** Quickdodge Flexors has the text "Defense Reaction -- \{r\}: Add this to the active chain link as a defending card. It has 2 base \{d\} this chain link." If Quickdodge Flexors is already defending card on the active chain link, then its ability is activated, it will remain a defending card on that chain link, no defend event will occur, but its base \{d\} will still be set to 2.

#### A defending card is considered to be defending against the active-attack on the chain link. If the active-attack ceases to exist, last known information about the active-attack is used to determine the properties, control, and ownership of the attack.[[rule:last_known_information]]

#### A card can only defend on one chain link for one attack-target at a time. If there are multiple attack-targets and an effect adds a defending card to a chain link but does not specify which attack-target it defends for, the controller of the effect determines which attack-target it will defend for.

#### If exactly one card is put onto a chain link as a defending card it is considered to defend alone. If two or more cards are put onto a chain link as defending cards in the same event, they are considered to defend together.

> **Example:** If a player declares two cards during the defend step of combat, those cards are considered to defend together. Then, if the player plays and resolves a defense reaction, that card is considered to defend alone because it is just one card being added as a defending card - despite there already being defending cards on the chain link.



## Layer Step @@sec:layer_step@@


### The Layer Step is a game state where an attack is unresolved on the stack.


### First, the turn player gains priority.


### Second and finally, when the top layer of the stack is the attack and all players pass in succession, the Layer Step ends and the Attack Step begins.



## Attack Step @@sec:attack_step@@


### The Attack Step is a game state where an attack resolves and becomes attacking before any defending cards are declared.


### @@rule:illegal_attack_target@@ First, at least one of the attack's attack-targets[[rule:attack_target]] must still be a legal target. Otherwise, the Attack Step ends and the Close Step begins[[sec:close_step]].

#### Only one target needs to be legal at this point of combat. If all attack-targets cease to be legal after this point, combat will continue.


### @@rule:becomes_chain_link@@ Second, each of the resolution abilities of the attack generates its effects in the order specified (except go again), and then the attack moves onto the combat chain as a chain link[[rule:chain_link]].

> **Note**: Attacks with resolution abilities that generate discrete effects printed before 2021 have received an errata that corrects them to be triggered effects that trigger when the attack becomes attacking.

#### If the attack is an attack-card, it moves onto the combat chain as a chain link. The attack-card is the active-attack.

> **Example:** Head Jab is an attack action card. After the Head Jab resolves, it moves as an attack-card onto the combat chain as a chain link, and it is considered the active-attack.

#### @@rule:attack_step_attack_proxy@@ If the attack is an attack-proxy, the attack and its attack-source move onto the combat chain as the chain link. The attack-proxy is the active-attack. If the attack-source was on a previous chain link, the attack-proxy on that chain link ceases to exist[[rule:attack_proxy_duration]].

> **Example:** Bone Basher is a one-handed weapon with an attack activated ability. After an attack-proxy of Bone Basher resolves, the attack-proxy and Bone Basher move onto the combat chain as a chain link, and the attack-proxy is considered the active-attack.

#### @@rule:attack_step_attack_layer@@  If the attack is an attack-layer, the card specified by the attack-layer's effect moves onto the combat chain as a chain link. This card is the active-attack. All of the parameters and applied effects of the attack-layer transfer to the active-attack, and then the attack-layer ceases to exist.

> **Example:** Emperor, Dracai of Aesir has the text "Search your deck for Command and Conquer, attack with it, then shuffle." After the ability resolves and Command and Conquer is found in the deck, the Command and Conquer moves to the combat chain as a chain link, and it is considered the active-attack.

#### @@rule:illegal_attack_source@@ If the active-attack does not exist, or cannot move to the combat chain as a chain link, the Attack Step ends and the Close Step begins[[sec:close_step]].

> **Example:** Emperor, Dracai of Aesir has the text "Search your deck for Command and Conquer, attack with it, then shuffle," where the active-attack is specified as the Command and Conquer. If the search fails to produce a Command and Conquer, the active-attack of the attack does not exist, so the combat chain closes.


### @@rule:attacking_object@@ Third, the active-attack is considered to be attacking until it leaves the combat chain. The "attack" event occurs and effects that trigger from attacking are triggered.

> **Example:** The attack is Dread Triptych. The abilities "When this attacks, if you've played a non-attack action card this turn, create a Runechant token." and "When this attacks, if you've dealt arcane damage this turn, create a Runechant token." trigger and are added as separate triggered-layers on the stack.

#### @@rule:attacking_hero@@ If there is an attack-source, and it is a living object [[rule:living_object]]), it becomes attacking. Otherwise, the controller of the attack and their hero card become the "attacking hero" until the active chain link resolves or the combat chain closes. If an effect of a source on the chain link refers to the attacking hero, it refers to that hero until the combat chain closes.

#### @@rule:defending_hero@@ If the attack-target is a hero, that hero and their controller become the "defending hero" until the active chain link resolves or the combat chain closes. If an effect of a source on the chain link refers to the defending hero, it refers to that hero until the combat chain closes.

> **Example:** Exude Confidence has the text "If this isn't defended by a card with greater or equal \{p\}, the defending hero can't play or activate instants and defense reactions," which is an effect that refers to the defending hero of the chain link where Exude Confidence the active-attack. If the next attack has a different attack-target, Exude Confidence's effect will still refer to that hero.


### Fourth, the turn player gains priority.


### Fifth and finally, when the stack is empty and all players pass in succession, the Attack Step ends and the Defend Step begins.



## Defend Step @@sec:defend_step@@


### The Defend Step is a game state where defending cards may be declared by a defending hero.


### @@rule:declare_defense@@ First, defending cards are declared for the attack-target(s). Cards declared this way become defending cards for the attack-target(s) on the active chain link[[rule:defending_card]]. Declaring a card this way is not considered playing that card - it does not incur the cost of playing that card, it does not add it as a layer on the stack, and it does not resolve any resolution abilities on that card.

#### If the attack-target is a hero (defending hero), their controller may declare any number of non-defense-reaction cards from their hand and/or public equipment permanents they control. Otherwise, a player may only declare cards for an attack-target if a rule or effect specifies it.

#### A card cannot be declared if (A) it does not have the defense property (0 is a value), (B) it is already a defending card on a chain link, or (C) it would make the current set of declared cards illegal to become defending.

> **Example:** If an attack has overpower (can't be defended by more than one action card) and is already defended by an action card, an action card cannot be declared because it cannot become a defending card.

#### If a player declares two or more defending cards for an attack-target, they decide the order those cards are declared and become defending.

> **Example:** Flic Flak has the text "If the next card you defend with this turn is a card with combo, it gains +2\{d\}." If a player declares two or more cards, they choose the order they become defending, and thus which of those cards Flic Flak's ability will apply to.

#### All declared cards for an attack-target are put onto the active chain link as a single compound event as defending cards for that attack-target. The order in which the declared cards become defending within the compound event is determined by the order in which were declared.[[rule:compound_event]]

> **Example:** Bastion of Unity has the text "Unity - When this defends together with a card from hand, this gets +1\{d\} until end of turn." If one player declares Bastion of Unity and another player declares a card from hand, Bastion of Unity's effect will trigger because both cards defend together as part of the same compound event.

#### If two or more players may declare defending cards for an attack-target, they do so in clockwise order starting with the player that controls the attack-target[[rule:clockwise_order]].

> **Example:** If a player's hero is attacked, that player declares any defending cards first, then in clockwise order, players may declare additional defending cards, such as cards with Protect.

#### If there are two or more attack-targets, defending cards are declared for each attack-target in clockwise order of their controller, starting from player that controls the attack[[rule:clockwise_order]]. Then, if two or more attack-targets are controlled by the same player, defending cards are declared for each attack-target in an order determined by that controlling player. Cards only defend the attack-target they are declared for. All declared cards for each attack target are put onto the active chain link in separate events as defending cards.

> **Example:** Apocalypse Automaton has the text "This attacks up to X target opposing heroes, [...]." If two players' heroes are attacked by an Apocalypse Automaton, the defending cards for each hero are declared in clockwise order from the controller of the attack. The first hero's player declares defending cards, then any player may declare additional defending cards (such as cards with Protect), and finally, those declared cards become defending cards for that hero. This process then repeats for the second hero.


### Second, the turn player gains priority.


### Third and finally, when the stack is empty and all players pass in succession, the Defend Step ends and the Reaction Step begins.



## Reaction Step @@sec:reaction_step@@


### The Reaction Step is a game state where players may use reactions related to combat.


### First, the turn player gains priority.

#### The attacking hero (if any) may play/activate attack reaction cards/abilities when they have priority during the Reaction Step.

#### The defending hero(es) (if any) may play/activate defense reaction cards/abilities when they have priority during the Reaction Step.

#### @@rule:defense_reaction_cant_play@@ A defense reaction card cannot be played if a rule or effect would prevent the player from defending with that card.

> **Example:** If an attack has dominate (can't be defended by more than 1 card from hand) and is already defended by a card from hand, defence reaction cards cannot be played from hand because dominate prevents it from becoming a defending card.

#### @@rule:resolve_defence_reaction@@ When a defense reaction card resolves it becomes a defending card on the active chain link for its controller's hero[[rule:defending_card]]. A defense reaction card fails to resolve if it cannot become a defending card[[rule:defense_reaction_fail]].

> **Example:** If an attack has dominate (can't be defended by more than 1 card from hand) and there are two defense reactions on the stack, the first one will resolve and become a defending card, but the second one will fail to resolve because dominate prevents it from becoming a defending card.


### Second and finally, when the stack is empty and all players pass in succession, the Reaction Step ends and the Damage Step begins.



## Damage Step @@sec:damage_step@@


### The Damage Step is a game state where the physical damage of the active chain link is calculated and applied.


### @@rule:calculate_damage@@ First, damage is calculated for the attack-target(s). If the power of the attack is greater than the sum total defense value of the defending cards for the attack-target, the attack deals \{p\} damage (physical damage) to the attack-target equal to the difference.

> **Example:** If the power of the attack is 6, and there are two defending cards with a defense 3 and 2 respectively then the sum total defense value of the defending cards is 5. The power of the attack is greater than the sum total defense, so the attack-target is dealt 6-5=1 \{p\} damage.

#### Dealing \{p\} damage to the attack-target this way, is a hit-event generated by the game ([[rule:hit]]). The source of the damage is the attack.

#### If the attack-target has ceased to exist or is illegal when the damage is calculated, no damage is dealt, and the event is not generated.

#### If there are two or more attack-targets, damage is calculated and dealt separately for each attack-target in an order determined by the controller of the attack.


### Second, the turn player gains priority.


### Third and finally, when the stack is empty and all players pass in succession, the Damage Step ends and the Resolution Step begins.


### @@rule:hit@@ An attack is considered to have hit if it deals damage to an attack-target during the Damage Step of combat. The hit-event is otherwise identical to a deal \{p\} damage event[[rule:damage_effect]] and only occurs during the Damage Step of combat.

#### If the attack-target loses life as a result of anything except damage dealt by the active-attack by the hit-event during the Damage Step of combat, then the attack is not considered to have hit.

#### If the hit-event is modified by replacement effects such that no damage is dealt by the active-attack to the attack-target, it is no longer a hit-event - the attack is not considered to have hit when the event occurs. Damage may still be dealt if the hit-event is modified, but it is not considered a hit-event if the active-attack is not the source of the damage that would be dealt to the attack-target.

> **Example:** Feign Death has the text "The next time you would be dealt damage this turn, prevent it." If the effect from Feign Death prevents all damage dealt by the active-attack, no damage is dealt, the hit-event does not occur, and the attack is not considered to have hit.

#### If a rule or effect prevents a triggered effect from triggering when the active-attack hits and/or when it deals damage, then the triggered effect does not trigger on the hit-event.

> **Example:** Stamp Authority has the text "Attack action card effects do not trigger when they hit," which prevents triggered effects from attack action card triggering on a hit-event. If a triggered effect from an attack action card would trigger on damage being dealt (e.g. Blizzard Bolt), and the attack action card hits, the effect will not trigger on the hit-event.

#### A chain link is considered to have hit if any hit-event occurs while it is the active chain link.



## Resolution Step @@sec:resolution_step@@


### The Resolution Step is a game state where the active chain link resolves and the attacker may gain an action point from go again and continue the combat chain by attacking.


### @@rule:chain_link_resolution@@ @@rule:combat_go_again@@ First, the active chain link becomes a resolved chain link and effects that trigger when the chain link resolves are triggered. If the attack has go again, its controller gains 1 action point.

#### If the attack is no longer on the combat chain, the last known information of the attack is used to determine whether the attack has go again.


### Second, the turn player gains priority. If an attack is added to the stack, the Resolution Step ends and the Layer Step begins.

#### The turn player may play or activate another attack during the Resolution Step, including attack action cards or abilities with attack.


### @@rule:close_combat_pass@@ Third and finally, when the stack is empty and all players pass in succession, the Resolution Step ends and the Close Step begins.



## Close Step @@sec:close_step@@


### The Close Step is a game state where the combat chain closes and combat ends. Players do not get priority during the Close Step.


### @@rule:closing_the_combat_chain@@ If a rule or effect causes the combat chain to close, the current step (if any) ends and the Close Step begins. The combat chain closes in the following situations:

#### If all players pass in succession when the stack is empty during the Resolution Step, the Close Step begins.[[rule:close_combat_pass]]

#### If there are no valid attack-targets at the beginning of the Attack Step, the Close Step begins.[[rule:illegal_attack_target]]

#### If the active-attack of the active chain link does not exist or cannot move to the combat chain as a chain link[[rule:illegal_attack_source]], or the active-attack ceases to exist before damage is calculated[[rule:calculate_damage]], the Close Step begins as a game state action.[[rule:game_state_action]]

> **Example:** Luminaris has the text "[...] Illusionist auras you control are weapons with 1\{p\} and "Once per Turn Action -- 0: Attack"." If a Spectral Shield token is activated to attack the opponent, and the token is destroyed before the Damage Step, the activated attack will also cease to exist, and the Close Step will begin.

#### If an effect closes the combat chain, the Close Step begins as a game state action.[[rule:game_state_action]]


### First, the "combat chain closes" event occurs and effects that trigger from the combat chain closing are triggered. All attacks and reactions on the stack, are put into their owner's graveyard.


### Second, layers on the stack resolve and game state actions are performed as if all players are passing priority in succession.[[rule:game_state_action]]


### Third, when the stack is empty, all permanents remaining on the combat chain return to their respective zones - equipment and weapons return to their respective equipped zones. Any other permanent returns to the permanent zone.


### Fourth, all remaining objects on the combat chain are cleared.[[rule:clear_definition]]


### Fifth and finally, the combat chain closes. Effects that last for "the/this combat chain" end. The Close Step ends and the Action Phase continues.