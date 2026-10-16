class AadapterNodeType(Enum):
    """
    Define types of nodes the adapter can provide
    """

    PROTEIN = auto()

class AdapterProteinField(Enum):
    """
    Define possible fields the adapter can provide for proteins
    """

    ID = "id"
    PREFERRED_ID = "preferred_id"
    GENE_SYMBOL = "genesymbol"
    NCBI_TAX_ID = "ncbi_tax_id"

class AdapterEdgeType(Enum):
    """
    Enum for the types of the protein adapter.
    """

    PROTEIN_PROTEIN_INTERACTION = "protein_protein_interaction"
    BINDING = "binding"
    ACTIVATION = "activation"
    PHOSPHORYLATION = "phosphorylation"
    UBIQUITINATION = "ubiquitination"
    INHIBITION = "inhibition"

class AdapterProteinProteinEdgeField(Enum):
    """
    Define possible fields the adapter can provide for protein-protein edges
    """

    INTERACTION_TYPE = ""
    INTERACTION_SOURCE = ""
    IS_DIRECTED = ""
    IS_STIMULATION = ""
    IS_INHIBITION = ""
    CONSENSUS_DIRECTION = ""
    CONSENSUS_STIMULATION = ""
    CONSENSUS_INHIBITION = ""
