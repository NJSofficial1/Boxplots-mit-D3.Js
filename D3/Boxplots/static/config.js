const CONFIG = {
    // ===== renderChart() =====
    margin: {top: 10, right: 30, bottom: 50, left: 40},
    width: 800,
    height: 600,
    // defines, which smallest/greatest values are no outliers as yet (which values are in whisker range)
    WhiskerFactor: 1.5,
    tooltipOffsetX: 10,
    tooltipOffsetY: 20,
    // ===== zoomInChart() =====
    marginZoomInChart: {top: 10, left: 40},
    // [min, max] scale factor of zooming
    scaleFactors: [1, 15],
    // ===== printOutliersBeforeFirstZoom =====
    marginOutliersBeforeFirstZoom: {top: 10, left: 40},
};