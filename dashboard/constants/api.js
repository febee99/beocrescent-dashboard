export const localBase = 'http://localhost';
export const devBase = 'https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev';
export const prodBase = '';


// change this if required
export const base = localBase;

export const tableVision = base == localBase ? ':5000/tables' : '/tables';
export const tableVisionStats = base == localBase ? ':5000/stats' : '/stats';
export const rfidFsrVision = base == localBase ? ':5000/rfid_fsr' : '';

export const rfidTrayInOut = base == localBase ? ':5000/tray_in_out' : '';
export const rfidTrayIn = base == localBase ? ':5000/tray_in' : '';

export const returnDistrVision = base == localBase ? ':5000/g6trayreturndistr' : '/g6trayreturndistr';
export const totalCountVision = base == localBase ? ':5000/g6total' : '/g6total';
export const barChart = base == localBase ? ':5000/g6barchart' : '/g6barchart';

export const g6Overview = base == localBase ? ':5000/g6overview' : '/g6overview';
export const overview2 = base == localBase ? ':5000/overview2' : '/overview2';
export const overview = base == localBase ? ':5000/overview/tray_return' : '/overview/tray_return';

export default {
    // base URL
    BASE: base,

    // Group 7 API endpoints
    TABLEVISION: tableVision,
    TABLEVISIONSTATS: tableVisionStats,
    RFIDFSRVISIO: rfidFsrVision,
    RFIDTRAYINOUT: rfidTrayInOut,
    RFIDTRAYIN: rfidTrayIn,

    // Group 6 API endpoints
    RETURNDISTRVISION: returnDistrVision,
    STALLTOTALVISION: totalCountVision,
    BARCHART: barChart,
    G6OVERVIEW: g6Overview,
    OVERVIEW2: overview2,

    OVERVIEW:overview

}