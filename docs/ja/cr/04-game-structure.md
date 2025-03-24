[REF book=CR chap=4]

# Game Structure @@cha:game_structure@@



## General @@sec:game_structure_general@@


### @@rule:game_definition@@ A game of Flesh and Blood is preceded by the start-of-game procedure and ends when a player wins or the game is a draw.[[sec:starting_a_game]][[sec:ending_a_game]]


### @@rule:match_definition@@ A match consists of one or more consecutive games between the same players with the same decks.


### @@rule:turn@@ A turn is a game state concept that structures the order of play and phases.

#### A turn consists of 3 phases in order: Start Phase, Action Phase, and End Phase.

#### @@rule:turn_player@@ Only one player can have a turn at any point in time. A player whose turn it is is the "turn player." A player whose turn it is not is a "non-turn player."



## Starting a Game @@sec:starting_a_game@@


### The process of starting a game is referred to as the start-of-game procedure. Players do not get priority during the start-of-game procedure.


### First, each player places their hero card face up in their hero zone.


### Second, a player is selected and chooses the first-turn player. If it is the first game of a match, one of the players is selected using a random method that is mutually agreeable. If it is not the first game of a match, the player who lost first in the previous game of the match is the selected player; or if the previous game ended in a draw, the selected player is the same as in the previous game. The select player then chooses any player to be the first-turn player.


### @@rule:select_starting_permanents@@ Third, each player selects arena-cards from their card-pool that they will start the game with.[[rule:arena_card]]

#### A player may select up to one arena-card for each of their arms, chest, head, legs, and weapon zones. Each card will start the game equipped in its respective zone, based on its type and/or subtype.[[rule:reveal_start]]

#### Cards selected this way are placed face-down in their respective zones or in a single face-down pile next to the hero. These cards and their number are private to each player until the game begins.


### @@rule:select_deck@@ Fourth, each player selects the deck-cards from their card-pool that will become their deck.

#### Arena-cards cannot be included in a player's deck.

#### If a meta-static ability effect allows the player to start the game with one or more cards in a zone other than their deck, these cards are selected from their deck and placed face-down in their respective zones or in the single face-down pile next to the hero. The cards selected this way are still considered part of the player's deck. These cards and their number are private to each player until the game begins.

> **Example:** Dash has the text "You may start the game with a Mechanologist item with cost \{r\}\{r\} or less in the arena," which means if the game format requires a starting deck of 40 cards, the player may select the specified from those 40 cards, and start the game with 1 card in the arena and 39 cards in their deck zone.


### @@rule:inventory@@ Fifth, all other cards in a player's card-pool that were not selected during [[rule:select_starting_permanents]] or [[rule:select_deck]] become that player's inventory.

#### An inventory is a defined collection of cards in the game - it is not a zone.

#### An inventory is private. Players may look at cards in their own inventory during a game but are not required to show any other player.

#### @@rule:inventory_removed_cards@@ If one or more cards remaining in the player's card-pool fail to meet the specifications of a rule or effect at the start of the game, those cards are removed from the game and are not considered part of the inventory for the game.

> **Example:** Taylor has the text "Each equipment in your starting inventory must have a different name," which means if there are two or more cards with the same name remaining in the player's card-pool, the first one is included in the player's inventory and the second one is removed from the game.


### Sixth, each player shuffles and presents their starting deck to an opponent to be shuffled and/or cut.

#### After a player has presented their starting deck to be shuffled and/or cut, it is placed in their deck zone and they may no longer change any cards they have chosen in [[rule:select_starting_permanents]][[rule:select_deck]].

#### A starting deck is private to each player. The opponent may not look at the information of the cards in a deck presented to them.


### @@rule:reveal_start@@ Seventh, each player in clockwise order equips their respective weapons and equipment, starting with the first turn player [[rule:clockwise_order]][[rule:equip_effect]]. Any other cards that start the game in a zone other than the deck zone are put in their respective zones. The "start of the game" event occurs and effects that trigger at the start of the game are triggered. Layers on the stack resolve and game state actions are performed as if all players are passing priority in succession until the stack is empty[[rule:game_state_action]].

#### If two or more triggered-layers are created, they are added to the stack in an order chosen by the first-turn player.[[rule:triggered_layer_order]]

#### If an effect would only trigger during a player's turn, it does not trigger during the start-of-game procedure.

> **Example:** Victor has the text "The first time each turn you create a Gold token from an effect you control, draw a card." If a player creates a Gold token from an effect they control during the start-of-game procedure, Victor's effect will not trigger because it is not during a player's turn.


### Eighth and finally, each player draws cards up to their hero's intellect and the first turn player begins their Start Phase.



## Start Phase @@sec:start_phase@@


### Players do not get priority during the Start Phase.


### First, the turn starts. Effects that last until the "start of turn" end. The "start of turn" event occurs and effects that trigger at the start of turn are triggered. Layers on the stack resolve and game state actions are performed as if all players are passing priority in succession until the stack is empty[[rule:game_state_action]].


### Second and finally, the Start Phase ends and the game proceeds to the action phase.



## Action Phase @@sec:action_phase@@


### First, the action phase starts. The "beginning of the action phase" event occurs and effects that trigger at the beginning of the action phase are triggered.


### Second, the turn player has 1 action point.

#### Effects that trigger when a player gains an action point do not trigger when the turn player gains an action point this way.

#### Replacement effects that modify events when a player gains an action point do not modify or replace when the turn player gains an action point this way.


### Third, the turn player gains priority.


### Fourth and finally, when the stack is empty, the combat chain is closed, and both players pass priority in succession, the action phase ends and the game proceeds to the End Phase.



## End Phase @@sec:end_phase@@


### Players do not get priority during the End Phase.


### First, the "beginning of the end phase" event occurs and effects that trigger at the beginning of the end phase are triggered. Layers on the stack resolve and game state actions are performed as if all players are passing priority in succession until the stack is empty.[[rule:game_state_action]].


### Second, the end-of-turn procedure occurs. After each step in the end-of-turn procedure, if a triggered effect has triggered, the triggered-layers are added to the stack; then layers on the stack resolve and game state actions are performed as if all players are passing priority in succession until the stack is empty. The end-of-turn procedure happens in the following order:

#### All allies' life totals are reset to their base life, modified by any counters on the object.

#### The turn player may put a card from their hand face-down into an empty arsenal zone they own.

#### Each player puts all cards in their pitch zone (if any) on the bottom of their deck in any order. The order cards are put on the bottom of the deck this way is hidden information.

#### All players lose all action points and resource points.

#### The turn player draws cards until the number of cards in their hand is equal to their hero's intellect \{i\}. If it is the first turn of the game, all other players draw cards until the number of cards in their hand is equal to their hero's intellect \{i\}. If a player already has at least that many cards in their hand, they do not draw any cards this way.[[rule:draw_effect]]


### Third and finally, the turn ends. Effects that last until the "until end of turn" and "this turn" end. The next player in clockwise order becomes the new turn player[[rule:clockwise_order]]. The new turn player begins their Start Phase.



## Ending a Game @@sec:ending_a_game@@


### A game ends immediately when a player wins, or the game is a draw.

#### @@rule:clear_losing_player@@ If a player loses a game, and the game does not end, all objects the player controls are cleared, and then all objects owned by the player are removed from the game. The player and their hero cease to exist for the remainder of the game. Layer-continuous effects controlled by the player continue to exist until they expire.

> **Example:** A player controls an attack action card on the combat chain and a triggered-layer on the stack. An opponent controls a Frostbite (a token-card) and a Frost Hex (a deck-card) owned by the player. If the player loses the game at this point, the attack is cleared to their graveyard and the triggered-layer ceases to exist on the stack, and then everything the player owns (including the Frostbite and Frost Hex) are removed from the game.


### A player can win the game in the following ways:

#### A player wins the game if all of their opponents have lost the game.

#### A player wins the game if an effect states that they win the game.


### A player can lose the game in the following ways:

#### A player loses the game if their hero's life total is reduced to zero or they do not control a hero.

#### A player loses the game if an effect states that they lose the game.

#### A player loses the game if they concede.


### The game can be a draw for the remaining players in the following ways:

#### The game is a draw for the remaining players if all remaining players' hero's life totals are simultaneously reduced to zero.

> **Example:** There are 2 remaining players. One player plays and resolves Forked Lightning, targeting both themselves and their opponent. Neither player prevents any arcane damage and both their life totals are simultaneously reduced to zero, resulting in a draw.

#### The game is a draw for the remaining players if an effect states that the game is a draw.

#### The game is a draw for the remaining players if all remaining players agree to an intentional draw. The remaining players can agree to a draw at any time.

#### The game is a draw for the remaining players if a stalemate occurs. A stalemate happens when no remaining player can legally advance the game state toward ending the game.

> **Example:** There are 2 remaining players. Both players only have a Cracked Bauble in their hand, no cards in the arena, or cards in their deck, arsenal, or banished zone. Both players control a weapon without an attack ability or an ability that would reduce life totals, so they have no way of advancing the game state to a conclusion. Therefore the game ends in a draw because both players are stalemated.

#### The game is a draw for the remaining players if a deadlock occurs. A deadlock happens when all remaining players refuse to legally advance the game state toward ending the game.

> **Example:** There are 2 remaining players on 1 life total. Both players only have Invert Existence and a Cracked Bauble in their hand, no equipment, weapon, or cards in their deck, arsenal, or banished zone. The first person to play Invert Existence will lose the game because the opposing player can respond with their Invert Existence which will resolve first and give them the win. Therefore the game ends in a draw because both players are deadlocked.
