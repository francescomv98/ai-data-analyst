from matplotlib.figure import Figure
from src.chart_generator import ChartGenerator
from src.dataframe_manager import DataFrameManager

def test_monthly_revenue_chart(sample_dataframe):
    """
    Test monthly revenue chart generation.
    """

    manager = DataFrameManager(sample_dataframe)

    monthly_data = manager.get_monthly_revenue()

    figure = ChartGenerator.plot_monthly_revenue(monthly_data)

    assert isinstance(figure, Figure)

def test_top_products_chart(sample_dataframe):
    """
    Test top products chart generation.
    """

    manager = DataFrameManager(sample_dataframe)

    products = manager.get_top_products()

    figure = ChartGenerator.plot_top_products(products)

    assert isinstance(figure, Figure)

def test_region_chart(sample_dataframe):
    """
    Test region chart generation.
    """

    manager = DataFrameManager(sample_dataframe)

    regions = manager.get_best_region()

    figure = ChartGenerator.plot_best_region(regions)

    assert isinstance(figure, Figure)