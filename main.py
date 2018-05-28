class engine():

  def __init__ (self):
    self.inp = ""
    self.out = ""
    self.ptr = 0
    self.mem = [0] * 64

  def run (self, code, inp): 
    self.inp = inp

    self.loop(code)

    print(self.mem)
    print(self.out)

    return

  def loop (self, code):
    i = -1

    while i < len(code) - 1:
      i += 1
      c = code[i]

      if c == "+":
        self.mem[self.ptr] += 1
      elif c == "-":
        self.mem[self.ptr] -= 1
      elif c == ">":
        self.ptr += 1
      elif c == "<":
        self.ptr -= self.ptr > 0 if 1 else 0
      elif c == ",":
        self.mem[self.ptr] = ord(self.inp[0])
        self.inp = self.inp[1:]
      elif c == ".":
        self.out += chr(self.mem[self.ptr])
      elif c == "[":
        ldepth  = 1
        li      = i
        lcode   = ""

        while ldepth > 0:
          li += 1
          i += 1
          c = code[li]

          if c == "[":
            ldepth += 1
          elif c == "]":
            ldepth -= 1

            if ldepth == 0:    
              while self.mem[self.ptr] > 0:
                self.loop(lcode)
              break  

          lcode += c
    return

program = """

"""

engine = engine()
engine.run(program,"")