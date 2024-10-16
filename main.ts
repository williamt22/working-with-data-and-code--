namespace SpriteKind {
    export const Environment = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    game.showLongText("Cave", DialogLayout.Bottom)
    B += 1
    game.showLongText("You've chosen the cave", DialogLayout.Bottom)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    A += 1
    adventure.addToTextlog("You've chosen tree!")
    pause(2000)
    adventure.clearTextLog()
})
let A = 0
let B = 0
// Begin of introduction
scene.setBackgroundColor(11)
adventure.addToTextlog("Welcome to Page Play! A choose your adventure video game with challenging decisions and surprising endings. ")
pause(2000)
adventure.clearTextLog()
adventure.addToTextlog("You can interact with this game using 'A' and 'B' to decide between two options. Restart to try different endings! ")
pause(2000)
adventure.clearTextLog()
game.splash("Your adventure awaits...")
let Tree = sprites.create(img`
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
    `, SpriteKind.Environment)
Tree.setPosition(80, 30)
Tree.setStayInScreen(true)
adventure.addToTextlog("You awaken in an open forest clearing, unsure how you ended up there. ")
pause(2500)
adventure.clearTextLog()
adventure.addToTextlog("You panic. Realising you had earlier been on a hike with your friends, which are now nowhere to be found. The sun is now almost set.")
pause(4000)
adventure.clearTextLog()
adventure.addToTextlog("In your surroundings you see a clearing between two trees, or a cave opening. Which will you choose?")
pause(4000)
adventure.clearTextLog()
game.showLongText("Tree (A)      Cave (B)", DialogLayout.Bottom)
