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

```python
```
