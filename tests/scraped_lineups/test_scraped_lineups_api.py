from signal_ocean.scraped_lineups import ScrapedLineup
from signal_ocean.util.parsing_helpers import _to_snake_case


def test_lineups_field_names():
    api_fields = [
        "LineupID",
        "MessageID",
        "ExternalMessageID",
        "ParsedPartID",
        "LineFrom",
        "LineTo",
        "InLineOrder",
        "Source",
        "UpdatedDate",
        "ReceivedDate",
        "IsDeleted",
        "ScrapedVesselName",
        "ScrapedIMO",
        "ScrapedDeadweight",
        "ScrapedYearBuilt",
        "IMO",
        "VesselName",
        "Deadweight",
        "YearBuilt",
        "LiquidCapacity",
        "VesselTypeID",
        "VesselType",
        "VesselClassID",
        "VesselClass",
        "CommercialOperatorID",
        "CommercialOperator",
        "ScrapedETA",
        "ETA",
        "ScrapedETB",
        "ETB",
        "ScrapedETD",
        "ETD",
        "ScrapedLocation",
        "LocationGeoID",
        "LocationName",
        "LocationTaxonomyID",
        "LocationTaxonomy",
        "OperationTypeID",
        "OperationType",
        "ScrapedQuantity",
        "Quantity",
        "QuantityUnit",
        "ScrapedCargoType",
        "CargoTypeID",
        "CargoType",
        "CargoGroupID",
        "CargoGroup",
        "ScrapedApiGravity",
        "ApiGravity",
        "ScrapedOrigin",
        "OriginGeoID",
        "OriginName",
        "OriginTaxonomyID",
        "OriginTaxonomy",
        "ScrapedDestination",
        "DestinationGeoID",
        "DestinationName",
        "DestinationTaxonomyID",
        "DestinationTaxonomy",
        "ScrapedSupplier",
        "SupplierID",
        "Supplier",
        "ScrapedCharterer",
        "ChartererID",
        "Charterer",
        "ScrapedBuyer",
        "BuyerID",
        "Buyer",
        "ScrapedPortAgent",
        "PortAgentID",
        "PortAgent",
        "VesselStatusID",
        "VesselStatus",
        "Content",
        "Subject",
        "Sender",
        "IsPrivate",
    ]
    snake_case_api_fields = list(map(_to_snake_case, api_fields))
    scraped_lineups_model_fields = list(ScrapedLineup.__dataclass_fields__)
    assert snake_case_api_fields == scraped_lineups_model_fields
