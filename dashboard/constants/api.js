export const localBase = 'http://localhost';
export const devBase = 'https://ui2lc3zrbc.execute-api.ap-southeast-1.amazonaws.com/dev';
export const prodBase = '';


// change this if required
export const base = localBase;

export const tableVision = base == localBase ? ':5000/tables' : '/tables';
export const rfidFsrVision = base == localBase ? ':5001/rfid_fsr' : '';
export const rfidTrayInOut = base == localBase ? ':5001/tray_in_out' : '';
export const rfidTrayIn = base == localBase ? ':5001/tray_in' : '';


export default {
    // base URL
    BASE: base,

    // API endpoitns
    TABLEVISION: tableVision,
    RFIDFSRVISIO: rfidFsrVision,
    RFIDTRAYINOUT: rfidTrayInOut,
    RFIDTRAYIN: rfidTrayIn,
   
}