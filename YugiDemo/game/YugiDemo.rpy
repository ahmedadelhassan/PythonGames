#This is a limited function demo for Duel of Heroes used for the 
#Kickstarter project
#The demo is made to look like Yugioh card game

init python:
    
    class YugiDemo(object):
        
        # We represent a card as a (suit, rank) tuple. The suit is one of the
        # following four constants, while the rank is 1 for ace, 2 for 2,
        # ..., 10 for 10, 11 for jack, 12 for queen, 13 for king.        
        DARK = 0
        LIGHT = 1
        WATER = 2
        AIR = 3
        
        def __init__(self, deal=1):
            
            # Constants to specify the positions of different
            # card stacks locations in the battlefield
            SHIFT = 100
            
            MONSTERS_XPOS = 480 
            MONSTERS_YPOS = 512 + SHIFT
            MONSTERS_SPACING = 80
            
            HERO_XPOS = 640
            HERO_YPOS = 618 + SHIFT
            
            MAGIC_XPOS = 560
            MAGIC_YPOS = 724 + SHIFT
            MAGIC_SPACING = 80
            
            GRAVEYARD_XPOS = 905
            GRAVEYARD_YPOS = 690 + SHIFT
            
            DECK_XPOS = 375
            DECK_YPOS = 690 + SHIFT
            
            HAND_XPOS = 440
            HAND_YPOS = 1024
            HAND_SPACING = 100
            
            # Store the parameters.
            self.deal = deal
            
            # Create the main tables for player one
            self.table_hand = hand_player_one = Table(base=None, back=None)
            self.table_field = field_player_one = Table(base="card/base.png", back="card/back.png")
            
            
            # Create the Hero
            self.hero = field_player_one.stack(HERO_XPOS, HERO_YPOS, xoff=0, yoff=0, drag=DRAG_NONE, click=True, drop=False)
            
            # Create the deck
            self.deck = field_player_one.stack(DECK_XPOS, DECK_YPOS, xoff=-0.2, yoff=0.2, click=True)
            
            # Creare the graveyard
            self.graveyard = field_player_one.stack(GRAVEYARD_XPOS, GRAVEYARD_YPOS, xoff=0, yoff=0, drag=DRAG_NONE, click=True, drop=False)
            
            # Create the monsters tableaus
            self.mosnters = [ ]
            for i in range(0, 5):
                s = field_player_one.stack(MONSTERS_XPOS + MONSTERS_SPACING * i, MONSTERS_YPOS, xoff=0, yoff=0, drag=DRAG_NONE, click=True, drop=False)
                self.mosnters.append(s)
            
            # Create the magic tableaus
            self.magic = [ ]
            for i in range(0, 3):
                s = field_player_one.stack(MAGIC_XPOS + MAGIC_SPACING * i, MAGIC_YPOS, xoff=0, yoff=0, drag=DRAG_NONE, click=True, drop=False)
                self.magic.append(s)
            
            # Create the hand tableaus
            self.hand = [ ]
            for i in range(0, 5):
                s = field_player_one.stack(HAND_XPOS + HAND_SPACING * i, HAND_YPOS, xoff=0, yoff=0, drag=DRAG_CARD, click=True, drop=True)
                self.hand.append(s)
                
            # Location of active card
            self.active = hand_player_one.stack(640, 512, xoff=0, yoff=0, drag=DRAG_NONE, click=True, drop=True)
                          
            # Fill the deck
            for rank in range(1, 40):
                value = rank
                field_player_one.card(value, "card/Hand1.jpg")
                field_player_one.set_faceup(value, False)
                self.deck.append(value)
            
            # Shuffle the deck
            self.deck.shuffle()
            
            
            
#        # This figures out the image filename for a given suit and rank.
#        def card_num(self, rank):
#            ranks = [ None ]
#            for i in range(1,40):
#                ranks.append(i)
#            return ranks[rank]
        
        def show(self):
            self.table_field.show()

        def hide(self):
            self.table_field.hide()

        def show_hand(self):
            self.table_hand.show()

        def hide_hand(self):
            self.table_hand.hide()

        def tableau_drag(self, evt):

            card = evt.drag_cards[0]
            cards = evt.drag_cards
            stack = evt.drop_stack

            csuit, crank = card
            
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table_field.set_sensitive(value)
            
#        # Draw card from deck
#        def draw_card(self, evt):
#            stack = evt.stack
#            for i in range(0, 5):
#                c = self.stack.deal()
#                self.hand[i].append(c)
                
        # Click deck to draw cards to empty slots in hand
        def draw_card(self, evt):

            if self.deck:
                for i in range(0, self.deal):
                    if self.deck:
                        for j in range (0, len(self.hand)):
                            # Check if hand slot is empty
                            if not self.hand[j]:
                                c = self.deck[-1]
                                self.table_field.set_faceup(c, True)
                                self.hand[j].append(c)

                
        # Click card in hand to appear full size
        def active_card(self, evt):
            if self.hand:
                c = evt.card
                ui.returns(c)
                return c
#                self.table_hand.show()
#                self.table_hand.set_faceup(c, True)
#                self.active.append(c)
                
                
                