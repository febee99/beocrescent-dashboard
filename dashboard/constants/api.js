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

export const returnVision = base == localBase ? ':5002/g6trayreturn' : '/g6trayreturn';
export const distrVision = base == localBase ? ':5002/g6traydistr' : '/g6traydistr';
export const totalCountVision = base == localBase ? ':5002/g6total' : '/g6total';

export const g6Overview = base == localBase ? ':5003/g6overview' : '/g6overview';

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
    STALLTOTALVISION: totalCountVision,
    G6OVERVIEW: g6Overview

}