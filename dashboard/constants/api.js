export const localBase = 'http://localhost';
export const devBase = 'https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev';
export const prodBase = '';


// change this if required
export const base = localBase;

export const tableVision = base == localBase ? ':5000/tables' : '/tables';
export const tableVisionStats = base == localBase ? ':5000/stats' : '/stats';
export const rfidFsrVision = base == localBase ? ':5008/rfid_fsr' : '';

export const rfidTrayInOut = base == localBase ? ':5008/tray_in_out' : '';
export const rfidTrayIn = base == localBase ? ':5008/tray_in' : '';

export const returnVision = base == localBase ? ':5002/g6trayreturn' : '';
export const distrVision = base == localBase ? ':5002/g6traydistr' : '';
export const totalCountVision = base == localBase ? ':5002/g6total' : '';

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
    RETURNVISION: returnVision,
    DISTRVISION: distrVision,
    STALLTOTALVISION: totalCountVision

}