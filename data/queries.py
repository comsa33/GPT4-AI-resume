FindAllFromWantedJobposting = """
    SELECT * FROM wanted_jobposting;
"""

FindDistinctCompanyNamesFromWantedJobpostingByPosition = """
    SELECT DISTINCT company_name FROM wanted_jobposting wj
        WHERE wj.position ILIKE :position;
"""

FindDistinctPositionFromWantedJobposting = """
    SELECT DISTINCT position FROM wanted_jobposting wj ;
"""

FindAllFromWantedJobpostingByPosition = """
    SELECT * FROM wanted_jobposting wj
        WHERE wj.position ILIKE :position;
    """

FindAllFromWantedJobpostingByCompanyName = """
    SELECT * FROM wanted_jobposting wj
        WHERE wj.company_name ILIKE :company_name;
    """

FindAllFromWantedJobpostingByCompanyNameAndPosition = """
    SELECT * FROM wanted_jobposting wj
        WHERE wj.company_name ILIKE :company_name
        AND wj.position ILIKE :position;
    """
