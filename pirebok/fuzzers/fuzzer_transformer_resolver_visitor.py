from functools import reduce
from operator import iconcat
from typing import Sequence

from pirebok.fuzzers.cmdi_fuzzer import CmdiFuzzer
from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.generic_fuzzer import GenericFuzzer
from pirebok.fuzzers.path_traversal_fuzzer import PathTraversalFuzzer
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer
from pirebok.fuzzers.xss_fuzzer import XssFuzzer
from pirebok.transformers import (
    CmdiTransformer,
    GenericTransformer,
    PathTraversalTransformer,
    SqlTransformer,
    Transformer,
    XssTransformer,
)


class FuzzerTransformerResolverVisitor(FuzzerVisitor):
    transformers: Sequence[Transformer]

    def visit_generic(self, fuzzer: GenericFuzzer) -> None:
        self.transformers = list(map(lambda x: x(), GenericTransformer.__subclasses__()))  # type: ignore

    def visit_sql(self, fuzzer: SqlFuzzer) -> None:
        self.transformers = reduce(
            iconcat,
            [
                list(map(lambda x: x(), SqlTransformer.__subclasses__())),  # type: ignore
                list(map(lambda x: x(), GenericTransformer.__subclasses__())),  # type: ignore
            ],
            [],
        )

    def visit_xss(self, fuzzer: XssFuzzer) -> None:
        self.transformers = reduce(
            iconcat,
            [
                list(map(lambda x: x(), XssTransformer.__subclasses__())),  # type: ignore
                list(map(lambda x: x(), GenericTransformer.__subclasses__())),  # type: ignore
            ],
            [],
        )

    def visit_cmdi(self, fuzzer: CmdiFuzzer) -> None:
        self.transformers = reduce(
            iconcat,
            [
                list(map(lambda x: x(), CmdiTransformer.__subclasses__())),  # type: ignore
                list(map(lambda x: x(), GenericTransformer.__subclasses__())),  # type: ignore
            ],
            [],
        )

    def visit_path_traversal(self, fuzzer: PathTraversalFuzzer) -> None:
        self.transformers = reduce(
            iconcat,
            [
                list(map(lambda x: x(), PathTraversalTransformer.__subclasses__())),  # type: ignore
                list(map(lambda x: x(), GenericTransformer.__subclasses__())),  # type: ignore
            ],
            [],
        )
