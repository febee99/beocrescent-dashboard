export const localBase = 'http://localhost';
export const devBase = 'https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev';
export const prodBase = '';


// change this if required
export const base = localBase;

export const tableVision = base == localBase ? ':5000/tables' : '/tables';
export const rfidFsrVision = base == localBase ? ':5001/rfid_fsr' : '';
export const trayReturnVision = base == localBase ? ':5002/g6trayreturn' : '';
export const trayReturnVision2 = base == localBase ? ':5002/g6trayreturn_s2' : '';

export default {
    // base URL
    BASE: base,

    // Group 7 API endpoitns
    TABLEVISION: tableVision,
    RFIDFSRVISIO: rfidFsrVision,

    // Group 6 API endpoints
    TRAYRETURNVISION: trayReturnVision,
    TRAYRETURNVISION2: trayReturnVision2
}