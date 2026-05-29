import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.university.pool',
  appName: 'Бассейн Университета',
  webDir: 'dist',  // ← ВАЖНО: должно быть 'dist'
  server: {
    androidScheme: 'https'
  }
};

export default config;