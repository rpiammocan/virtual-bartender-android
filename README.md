# Virtual Bartender for Android

![Virtual Bartender](assets/virtual-bartender-icon.svg)

Standalone Android edition of Virtual Bartender for phones and tablets.

## 🤖 Download the Android APK

### ⬇️ [Open the latest Android APK builds](https://github.com/rpiammocan/virtual-bartender-android/actions/workflows/build-android.yml)

Open the newest successful **Build Android APK** run, scroll to **Artifacts**, and download **VirtualBartender-Android-Offline**. Extract the ZIP and install `VirtualBartender-Android-Offline.apk` on your Android device.

[View all Android build runs](https://github.com/rpiammocan/virtual-bartender-android/actions/workflows/build-android.yml) · [View the CasaOS edition](https://github.com/rpiammocan/virtual-bartender-casaos) · [View the Windows edition](https://github.com/rpiammocan/virtual-bartender-windows)

## Current features

- Cocktail and mocktail recipes
- My Bar inventory
- Tonight's Bar
- What Can I Make matching
- Clickable recipe links from every What Can I Make category
- Ingredient substitutions and recipe variants
- Shopping list and suggestions
- Favorites and history
- Surprise Me
- Android-local persistent data
- Standalone offline operation

## Architecture

- React interface reused from the CasaOS edition through a deliberately pinned source revision
- Capacitor native Android container
- Android-local persistent data layer replacing the CasaOS `/api` backend
- Offline recipes, inventory, favorites, history, shopping list, Tonight's Bar, and matching

## Source snapshot

`source-pin.json` records the exact CasaOS source revision used as the UI starting point. Android builds do not automatically follow CasaOS `main`, keeping the Android edition isolated until changes are deliberately brought over.

## APK builds

GitHub Actions builds an installable debug APK with Gradle. Android's debug APK is automatically signed by the Android build tools and can be installed directly for testing.

## Edition separation

- [CasaOS](https://github.com/rpiammocan/virtual-bartender-casaos)
- [Windows](https://github.com/rpiammocan/virtual-bartender-windows)
- **Android — this repository**
