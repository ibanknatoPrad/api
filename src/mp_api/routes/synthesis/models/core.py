from enum import Enum
from typing import List

from pydantic import BaseModel, Field
from pymatgen.core import Composition

from mp_api.routes.synthesis.models.materials import ExtractedMaterial
from mp_api.routes.synthesis.models.operations import Operation
from mp_api.routes.synthesis.models.reaction import ReactionFormula


class SynthesisTypeEnum(str, Enum):
    solid_state = "solid-state"
    sol_gel = "sol-gel"


class SynthesisRecipe(BaseModel):
    """
    Model for a document containing synthesis description data
    """

    # Basic facts about this recipe:
    doi: str = Field(
        ...,
        description="DOI of the journal article.",
    )
    paragraph_string: str = Field(
        "",
        description="The paragraph from which this recipe is extracted."
    )
    synthesis_type: SynthesisTypeEnum = Field(
        ...,
        description="Type of the synthesis recipe."
    )

    # Reaction related information:
    reaction_string: str = Field(
        ...,
        description="String representation of this recipe."
    )
    reaction: ReactionFormula = Field(
        ...,
        description="The balanced reaction formula."
    )

    target: ExtractedMaterial = Field(
        ...,
        description="The target material."
    )
    targets_formula: List[str] = Field(
        ...,
        description="List of synthesized target material compositions."
    )
    precursors_formula: List[str] = Field(
        ...,
        description="List of precursor material compositions."
    )
    targets_formula_s: List[str] = Field(
        ...,
        description="List of synthesized target material compositions, as strings."
    )
    precursors_formula_s: List[str] = Field(
        ...,
        description="List of precursor material compositions, as strings."
    )

    precursors: List[ExtractedMaterial] = Field(
        ...,
        description="List of precursor materials."
    )

    operations: List[Operation] = Field(
        ...,
        description="List of operations used to synthesize this recipe."
    )