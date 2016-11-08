# Principios Fundamentales de la Programación
A continuación se explican porque los siguientes ejemplos son una buena representación de su principio.

## Curly's Law
Una variable debe tener un  y sólo un significado, este debe ser el mismo durante todo el código.

### Bad
La siguiente clase tiene demasiadas funcionalidades no unicas, y se utiliza para diversos propositos, como serializar a `string` o bien almacenar en la base de datos.
```python
class Employee():
    def calculatePay(self, price)
    def reportHours(self)
    def increaseHours(self, hours)
    def hoursToString(self)
    def save(self)
```
### Solución: Curly's Law
Separar de acuerdo a una única funcionalidad.
```python
class Employee():
    def calculatePay(price)
    def reportHours()
    def increaseHours(hours)

class StringMapper():
    def hoursToString(name, hours)

class Database():
  def SaveEmployee(name, hours)
```
## Command Query Segregation
Cada método debe ser un comando que ejecute una acción en específico o una consulta que retorna información, pero no ambas al mismo tiempo.

### Bad
La siguiente función almacena y retorna el estado del objeto.
```python
  def write_page(data):
      self.pages[self.actual_page] = data
      self.actual_page += 1
      return self.pages
```
### Solución: Command Query Segregation

```python
  def write_page(self, data):
      self.pages[self.actual_page] = data
      self.actual_page += 1

  def get_pages(self):
      return self.pages

```

## Boy Scout Rule
Al hacer cambios a código existente se tiende a degradar la calidad del mismo debido a la acumuluación de falencias técnicas.

### Bad
Del código anterior, al añadir más funcionalidades sobre el mismo mal código.

```python
    def write_page(self, data):
        self.pages[self.actual_page] = data
        self.actual_page += 1
        for number, page in self.pages.items():
            self.pages[number] = page + "This was page {}".format(number)
        return self.pages
```

### Solución: Boy Scout Rule
Hacer refactory del código.
```python
    def write_page(self, data)
    def get_pages(self)
    def add_number_page(self)
```

## KISS
El evitar la complejidad y buscar la simplicidad debe ser siempre una meta fija.

### Bad
Una sumatoria hasta `n` de forma recursiva. Lo que todos siempre hemos necesitado.
```python
def sum(n, first=0):
    if n == first:
        return 0
    else:
        return n + sum(n-1, (n+first)//2) + sum((n+first)//2, first)

```

### Solución: Keep it simple stupid!
Simplemente hacemos el calculo de la sumatoria.
```python
def sum(n):
    return n*(n+1)/2
```

## DRY
Cada pieza dentro de un sistema debe tener una única e inequívoca representación dentro de un sistema.

### Bad
Código repetido
```python
    def increase(self, e):
        for element in self.lista:
            if e == element:
                element += 1

    def decrease(self, e):
        for element in self.lista:
            if e == element:
                element -= 1

    def duplicate(self, e):
        for element in self.lista:
            if e == element:
                element *= 2
```

### Solución: DRY
Crear métodos para encapsular las funcionalidades repetidas.
```python
    def find(self, e):
        for element in self.lista:
            if element == e:
                return element
```
