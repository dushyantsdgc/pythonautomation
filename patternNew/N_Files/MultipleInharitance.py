class Pokemon:
    def move_Cartoon_fw(self):
        print("Move Forward")
    def move_Cartoon_bw(self):
        print("Move Backward")

class ChotaBheem:
    def jump_Cartoon_fw(self):
        print("Jump Forward")
    def jump_cartoon_bw(self):
        print("Jump Backward")

class Moguli(Pokemon,ChotaBheem):
    pass

Activity = Moguli()
Activity.move_Cartoon_fw()
Activity.jump_Cartoon_fw()

class Tomy(Moguli):
    def move_Cartoon_bw(self):
        print("Dog is barking")

Bark = Tomy()
Bark.move_Cartoon_bw()
Bark.jump_cartoon_bw()