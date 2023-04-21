""" Day 7: Some Assembly Required

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!
Unfortunately, little Bobby is a little under the recommended age range, and he needs help
assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal
(a number from 0 to 65535). A signal is provided to each wire by a gate, another wire,
or some specific value. Each wire can only get a signal from one source, but can provide
its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means
to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

  * 123 -> x means that the signal 123 is provided to wire x.
  * x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
  * p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
  * NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason,
you'd like to emulate the circuit instead, almost all programming languages (for example,
C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:
  123 -> x
  456 -> y
  x AND y -> d
  x OR y -> e
  x LSHIFT 2 -> f
  y RSHIFT 2 -> g
  NOT x -> h
  NOT y -> i

After it is run, these are the signals on the wires:
  d: 72
  e: 507
  f: 492
  g: 114
  h: 65412
  i: 65079
  x: 123
  y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is
ultimately provided to wire a?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires
(including wire a). What new signal is ultimately provided to wire a?
"""

import collections
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique
from typing import DefaultDict, Dict, List, Optional, Set, Union, Iterable, Callable, MutableMapping


Wire = str
Storage = Dict[Wire, int]


@unique
class OperationName(Enum):
    """ Название операции """
    op_assign = 'ASSIGN'
    op_and = 'AND'
    op_lshift = 'LSHIFT'
    op_not = 'NOT'
    op_or = 'OR'
    op_rshift = 'RSHIFT'


# Коды операций для присвоения одного значения сигнала проводника другому
AssignOperations: MutableMapping[OperationName, Callable] = {
    OperationName.op_assign: lambda x, _: x,
}

# Коды операций с двумя операндами
BinaryOperations: MutableMapping[OperationName, Callable] = {
    OperationName.op_and: lambda x, y: x & y,
    OperationName.op_lshift: lambda x, y: x << y,
    OperationName.op_or: lambda x, y: x | y,
    OperationName.op_rshift: lambda x, y: x >> y,
}

# Коды операций с одним операндом
UnaryOperations: MutableMapping[OperationName, Callable] = {
    OperationName.op_not: lambda x, _: 2 ** 16 - (x + 1),
}


@unique
class OperandType(Enum):
    """ Тип операнда (переменная или константа) """
    literal = 'literal'
    wire = 'wire'


OperandValue = Union[int, Wire]


class Operand:
    """ Описание операнда """

    def __init__(self, type: OperandType, value: OperandValue) -> None:
        self.type: OperandType = type
        self._value: OperandValue = value

    def value(self, storage: Storage) -> Optional[int]:
        """ Возвращает фактическое значение операнда """
        if self.type == OperandType.literal:
            return self._value
        return storage[self._value]

    def wire(self) -> Optional[str]:
        """ Возвращает название проводника (если есть) """
        return self._value if self.type == OperandType.wire else None

    @classmethod
    def from_str(cls, value: Optional[str]) -> Optional['Operand']:
        """ Возвращает операнд исходя из строкового представления """

        if not value:
            return None

        if value.isdigit():
            return cls(type=OperandType.literal, value=int(value))

        return cls(type=OperandType.wire, value=value)


@dataclass(frozen=True)
class Command(ABC):
    """ Команда на изменение сигнала проводников """

    result_wire: Wire
    first_operand: Operand
    second_operand: Optional[Operand] = None

    @abstractmethod
    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        raise NotImplementedError()

    @property
    def first_wire(self) -> Optional[Wire]:
        """ Возвращает название первого проводника """
        return self.first_operand.wire()

    @property
    def second_wire(self) -> Optional[Wire]:
        """ Возвращает название второго проводника """
        return self.second_operand.wire() if self.second_operand else None

    @classmethod
    def build(
            cls,
            result_wire: str,
            first_operand: str,
            second_operand: Optional[str] = None,
    ) -> 'Command':
        """ Возвращает команду в структурированном виде """

        return cls(
            result_wire=result_wire,
            first_operand=Operand.from_str(first_operand),
            second_operand=Operand.from_str(second_operand),
        )

    @staticmethod
    def _value(self, operand: Operand, storage: Storage) -> int:
        """ Возвращает фактическое значение операнда """


class AndCommand(Command):
    """ Обработка команды AND """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        first, second = self.first_operand.value(storage), self.second_operand.value(storage)
        return first & second


class AssignCommand(Command):
    """ Обработка  """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        return self.first_operand.value(storage)


class LShiftCommand(Command):
    """ Обработка команды LSHIFT """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        first, second = self.first_operand.value(storage), self.second_operand.value(storage)
        return first << second


class NotCommand(Command):
    """ Обработка команды NOT """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        first = self.first_operand.value(storage)
        return 2 ** 16 - (first + 1)


class OrCommand(Command):
    """ Обработка команды OR """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        first, second = self.first_operand.value(storage), self.second_operand.value(storage)
        return first | second


class RShiftCommand(Command):
    """ Обработка команды RSHIFT """

    def execute(self, storage: Storage) -> int:
        """ Выполнение команды """
        first, second = self.first_operand.value(storage), self.second_operand.value(storage)
        return first >> second


def _command_factory(
        operation: str,
        result_wire: str,
        first_operand: str,
        second_operand: Optional[str] = None,
) -> Command:
    """ Фабрика создания команд """

    name = OperationName((operation or '').strip().upper())

    command_cls = {
        OperationName.op_assign: AssignCommand,
        OperationName.op_and: AndCommand,
        OperationName.op_lshift: LShiftCommand,
        OperationName.op_not: NotCommand,
        OperationName.op_or: OrCommand,
        OperationName.op_rshift: RShiftCommand,
    }[name]

    return command_cls.build(
        result_wire=result_wire,
        first_operand=first_operand,
        second_operand=second_operand,
    )


def _topological_sort(commands: List[Command], destination: str) -> List[Command]:
    """ Топологическая сортировка команд """

    indexed_commands = {cmd.result_wire: cmd for cmd in commands}
    graph: DefaultDict[str, Set[str]] = collections.defaultdict(set)
    result = []
    seen = set()

    def recursive_helper(wire):
        for neighbor in graph[wire]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.append(indexed_commands[wire])

    # Построение графа зависимостей
    for result_wire, cmd in indexed_commands.items():
        if cmd.first_wire:
            graph[result_wire].add(cmd.first_wire)
        if cmd.second_wire:
            graph[result_wire].add(cmd.second_wire)

    recursive_helper(destination)
    result.append(indexed_commands[destination])

    return result


class Simulator:
    """ Имитатор выполнения команд прохождения сигнала """

    def __init__(self, storage: Storage, commands: List[Command]) -> None:
        self.storage: Storage = storage
        self.commands: List[Command] = commands

    def run(self, result_wire: Wire) -> int:
        """ Выполнение команд прохождения сигнала """

        for cmd in _topological_sort(self.commands, destination=result_wire):
            self.storage[cmd.result_wire] = cmd.execute(self.storage)

        return self.storage[result_wire]


def _parse_input(string: str) -> Command:
    """ Возвращает сформированную команду исходя из строкового представления """

    binary_keywords = '|'.join(keyword.value for keyword in BinaryOperations)
    unary_keywords = '|'.join(keyword.value for keyword in UnaryOperations)

    binary_operation_template = r'(\w+)\s+({})\s+(\w+) -> (\w+)'.format(binary_keywords)
    if (match := re.match(binary_operation_template, string)) is not None:
        return _command_factory(
            first_operand=match.group(1),
            operation=match.group(2),
            second_operand=match.group(3),
            result_wire=match.group(4),
        )

    unary_operation_template = r'({})\s+(\w+) -> (\w+)'.format(unary_keywords)
    if (match := re.match(unary_operation_template, string)) is not None:
        return _command_factory(
            first_operand=match.group(2),
            operation=match.group(1),
            result_wire=match.group(3),
        )

    assign_operation_template = r'(\w+) -> (\w+)'
    if (match := re.match(assign_operation_template, string)) is not None:
        return _command_factory(
            first_operand=match.group(1),
            operation=OperationName.op_assign.value,
            result_wire=match.group(2),
        )

    raise ValueError(f'Wrong command: {string}')


def first_task(strings: Iterable[str], result_wire: str) -> int:
    """ Решение первой задачи """

    storage = {}

    # Формирование списка команд
    # Для дальнейшей обработки необходимо считать все команды
    commands = [_parse_input(string) for string in strings]

    # Имитация прохождения сигнала через контакты
    return Simulator(storage, commands).run(result_wire=result_wire)
