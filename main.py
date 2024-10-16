@namespace
class SpriteKind:
    Environment = SpriteKind.create()

def on_b_pressed():
    global B
    game.show_long_text("Cave", DialogLayout.BOTTOM)
    B += 1
    game.show_long_text("You've chosen the cave", DialogLayout.BOTTOM)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global A
    game.show_long_text("Tree", DialogLayout.BOTTOM)
    A += 1
    game.show_long_text("You've chosen the tree", DialogLayout.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

A = 0
B = 0
# Begin of introduction
scene.set_background_color(13)
game.show_long_text("Welcome to Page Play! A choose your adventure video game with challenging decisions and surprising endings. ",
    DialogLayout.CENTER)
game.show_long_text("You can interact with this game using 'A' and 'B' to decide between two options. Restart to try different endings! ",
    DialogLayout.CENTER)
game.splash("Your adventure awaits...")
Tree = sprites.create(img("""
        ........................
            8..........ff..........8
            68........f88f........86
            688......ff88ff......886
            668......f8888f......866
            6668....f888888f....8666
            666688ff88888888ff886666
            666666888888888888666666
            666668888888888888866666
            666666888888888888666666
            66888668f88888ff86688666
            8668688888fff88f88886688
            8868668f8ff8ff8f88686886
            8888868fff88ffff86688866
            88888888ff8fffff86888868
            888668888ffffff888866888
            68886668ffff8fff86668888
            6868866688f88f8866688686
            6866666688888f8666666666
            666666666888886686666666
            666666668688888866666666
            666666666888888666666666
            6866668666888f8866866686
            6886866886688f8688668886
            866888688888f86688688686
            8866888868ff866886886688
            88868688668f888866866888
            88888668868ff88888888888
            68868868688f888666886688
            668666666688886668866688
            666666666668866666666686
            666668666888888666866666
            666666888888888888668666
            6668868ff88f888ff8688668
            8668888ff8fff88fff888688
            e88......ffeeff......88e
            eef......feeeef......fee
            eef......feeeef......fee
            feef....feeefeef....feee
            ffef....fefeffef....fefe
    """),
    SpriteKind.Environment)
Tree.set_position(80, 30)
Tree.set_stay_in_screen(True)
game.show_long_text("You awaken in an open forest clearing, unsure how you ended up there. ",
    DialogLayout.BOTTOM)
Tree.set_image(img("""
    ................................
        ................................
        ................................
        ................................
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ................................
        ................................
        ................................
        ..............fff...............
        ..............fff...............
        ..............fff...............
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
"""))
game.show_long_text("You panic. Realising you had earlier been on a hike with your friends, which are now nowhere to be found. The sun is now almost set.",
    DialogLayout.BOTTOM)
game.show_long_text("In your surroundings you see a clearing between two trees, or a cave opening. Which will you choose?",
    DialogLayout.BOTTOM)