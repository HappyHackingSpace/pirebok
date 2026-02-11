from abc import ABC, abstractmethod

from pirebok.fuzzers.cmdi_fuzzer import CmdiFuzzer
from pirebok.fuzzers.generic_fuzzer import GenericFuzzer
from pirebok.fuzzers.path_traversal_fuzzer import PathTraversalFuzzer
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer
from pirebok.fuzzers.xss_fuzzer import XssFuzzer


class FuzzerVisitor(ABC):
    @abstractmethod
    def visit_generic(self, fuzzer: GenericFuzzer) -> None:
        pass

    @abstractmethod
    def visit_sql(self, fuzzer: SqlFuzzer) -> None:
        pass

    @abstractmethod
    def visit_xss(self, fuzzer: XssFuzzer) -> None:
        pass

    @abstractmethod
    def visit_cmdi(self, fuzzer: CmdiFuzzer) -> None:
        pass

    @abstractmethod
    def visit_path_traversal(self, fuzzer: PathTraversalFuzzer) -> None:
        pass
