#!/usr/bin/env python
# -*- coding: utf-8 -*-
import database as db


class EightQueens:
  #def __init__(self, size):
  def __init__(self, size=None):
    self.min_option = 8
    self.size = size
    self.solutions = 0
    self.test = False
    self.solutions_puzzle()

  # Generar tablero con las reinas
  def board(self, positions):
    complete_board = ""

    for row in range(self.size):
      line = ""
      for column in range(self.size):
        if positions[row] == column:
            line += "Q "
        else:
            line += "_ "
      complete_board += line + "\n"
    return complete_board

  # Verificar lugar válido en el tablero para colocar una reina
  def check_place(self, positions, ocuppied_rows, column):
    for i in range(ocuppied_rows):
      if positions[i] == column or \
        positions[i] - i == column - ocuppied_rows or \
        positions[i] + i == column + ocuppied_rows:
        return False
    return True

  # Colocar reina en el tablero en un lugar válido
  def place_queen(self, positions, current_row):
    if current_row < self.size:
      for column in range(self.size):
        if self.check_place(positions, current_row, column):
          positions[current_row] = column
          next_row = current_row + 1
          self.place_queen(positions, next_row)
    else:
      # Obtener solución y guardarla en la base de datos
      complete_board = self.board(positions)
      
      if not self.test:
        data = {"solucion": str(complete_board)}
        database_class = db.Database()
        database_class.saveData(data)
      self.solutions += 1

  # Obtener las soluciones
  def solutions_puzzle(self):
    if self.size is None:
      print("Por favor ingrese un número entero igual o mayor a 8:")
      number = input()

      if number.isdigit() and int(number) >= self.min_option:
        self.size = int(number)
        positions = [1] * self.size
        self.place_queen(positions, 0)
        print(self.solutions, "soluciones encontradas.")
      else:
        self.solutions_puzzle()
    else:
      self.test = True
      positions = [1] * int(self.size)
      self.place_queen(positions, 0)

def main():
  EightQueens()

if __name__ == "__main__":
  main()