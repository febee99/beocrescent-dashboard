export const localBase = 'http://localhost';
export const devBase = 'https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev';
export const prodBase = '';


// change this if required
export const base = localBase;

export const tableVision = base == localBase ? ':5000/tables' : '/tables';
export const tableVisionStats = base == localBase ? ':5000/stats' : '/stats';
export const rfidFsrVision = base == localBase ? ':5001/rfid_fsr' : '';

export const rfidTrayInOut = base == localBase ? ':5001/tray_in_out' : '';
export const rfidTrayIn = base == localBase ? ':5001/tray_in' : '';

export const trayReturnVision = base == localBase ? ':5002/g6trayreturn' : '';
export const trayReturnVision2 = base == localBase ? ':5002/g6trayreturn_s2' : '';

export const trayDistrVision = base == localBase ? ':5002/g6traydistr' : '';
export const trayDistrVision2 = base == localBase ? ':5002/g6traydistr_s2' : '';

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
    HAICHEWRETURNVISION: trayReturnVision,
    HAICHEWDISTRVISION: trayDistrVision,

    SOONHENGRETURNVISION: trayReturnVision2,
    SOONHENGDISTRVISION: trayDistrVision2

}