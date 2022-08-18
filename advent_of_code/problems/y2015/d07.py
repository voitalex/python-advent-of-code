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
from dataclasses import dataclass
from enum import Enum, unique
from typing import DefaultDict, Dict, Iterable, List, Optional, Set, Union, Any


@unique
class OperandTypeEnum(Enum):
    """ Тип операнда (переменная или константа) """
    literal = 'literal'
    wire = 'wire'


@unique
class OperationCodeEnum(Enum):
    """ Код операции """
    op_and = 'AND'
    op_assign = 'ASSIGN'
    op_lshift = 'LSHIFT'
    op_not = 'NOT'
    op_or = 'OR'
    op_rshift = 'RSHIFT'


@unique
class OperationTypeEnum(Enum):
    """ Классификация операций по количеству операндов """
    assign = 'assign'
    unary = 'unary'
    binary = 'binary'


OperandValue = Union[str, int]


@dataclass(frozen=True)
class Operand:
    """ Описание операнда """
    op_type: OperandTypeEnum
    value: OperandValue


@dataclass(frozen=True)
class Command:
    """ Описание команды """
    left: Operand
    right: Optional[Operand]
    operation: OperationCodeEnum
    result: str
    op_type: OperationTypeEnum


def _bitwise_complement(value: int, bit_length: int = 16) -> int:
    """ Возвращает логическое дополнение до 1 """
    power_of_2: int = 2 ** bit_length
    return power_of_2 - (value + 1)


def _execute(cmd: Command, state: Dict[str, Any]) -> Dict[str, Any]:
    """ Выполнение команды """

    def get_operand_value(operand: Operand) -> int:
        """ Возвращает значение операнда команды """

        if operand.op_type == OperandTypeEnum.literal:
            return operand.value

        try:
            return state[operand.value]
        except LookupError as error:
            raise ValueError(f'Reference to undefined wire {operand.value}') from error

    def assign_operation() -> int:
        """ Выполнение команды присваивания """
        return get_operand_value(cmd.left)

    def unary_operation() -> int:
        """ Выполнение команды из одного операнда """
        value = get_operand_value(cmd.left)
        if cmd.operation == OperationCodeEnum.op_not:
            return _bitwise_complement(value)
        raise ValueError('Unknown operation')

    def binary_operation() -> int:
        """ Выполннение команды из двух операндов """

        left_value = get_operand_value(cmd.left)
        right_value = get_operand_value(cmd.right)

        if cmd.operation == OperationCodeEnum.op_and:
            return left_value & right_value
        if cmd.operation == OperationCodeEnum.op_or:
            return left_value | right_value
        if cmd.operation == OperationCodeEnum.op_lshift:
            return left_value << right_value
        if cmd.operation == OperationCodeEnum.op_rshift:
            return left_value >> right_value

        raise ValueError('Unknown operation')

    result = {
        OperationTypeEnum.assign: assign_operation,
        OperationTypeEnum.unary: unary_operation,
        OperationTypeEnum.binary: binary_operation,
    }[cmd.op_type]()

    return {**state, **{cmd.result: result}}


def _parse_operand(value: str) -> Operand:
    """ Возвращает значение операнда """
    if value.isdigit():
        return Operand(op_type=OperandTypeEnum.literal, value=int(value))
    return Operand(op_type=OperandTypeEnum.wire, value=value)


def _parse_input(string: str) -> Command:
    """ Возвращает сформированную команду исходя из строкового представления """

    binary_operation_template = r'(\w+)\s+(AND|OR|LSHIFT|RSHIFT)\s+(\w+) -> (\w+)'
    if (match := re.match(binary_operation_template, string)) is not None:
        return Command(
            left=_parse_operand(match.group(1)),
            operation=OperationCodeEnum(match.group(2)),
            right=_parse_operand(match.group(3)),
            result=match.group(4),
            op_type=OperationTypeEnum.binary,
        )

    unary_operation_template = r'(NOT)\s+(\w+) -> (\w+)'
    if (match := re.match(unary_operation_template, string)) is not None:
        return Command(
            left=_parse_operand(match.group(2)),
            operation=OperationCodeEnum(match.group(1)),
            right=None,
            result=match.group(3),
            op_type=OperationTypeEnum.unary,
        )

    assign_operation_template = r'(\w+) -> (\w+)'
    if (match := re.match(assign_operation_template, string)) is not None:
        return Command(
            left=_parse_operand(match.group(1)),
            operation=OperationCodeEnum.op_assign,
            right=None,
            result=match.group(2),
            op_type=OperationTypeEnum.assign,
        )

    raise ValueError(f'Wrong command: {string}')


def _topological_sort(commands: List[Command], destination: str) -> List[Command]:
    """ Топологическая сортировка команд """

    indexed_commands = {cmd.result: cmd for cmd in commands}
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
        if cmd.left is not None and cmd.left.op_type == OperandTypeEnum.wire:
            graph[result_wire].add(cmd.left.value)
        if cmd.right is not None and cmd.right.op_type == OperandTypeEnum.wire:
            graph[result_wire].add(cmd.right.value)

    recursive_helper(destination)
    result.append(indexed_commands[destination])

    return result


def first_task(strings: Iterable[str], wire: str = 'a') -> int:
    """ Решение первой задачи """

    wire_state: Dict[str, int] = {}

    # Получение и формирование команд
    commands = [_parse_input(string) for string in strings]

    # Выполнение команд
    for command in _topological_sort(commands=commands, destination=wire):
        wire_state = _execute(command, state=wire_state)

    return wire_state[wire]
