# Virtual Bartender for Android

Android edition of Virtual Bartender.

This repository is intentionally separate from both the CasaOS/Docker and Windows editions.

## Goal

Produce a directly installable Android APK that runs Virtual Bartender locally on a phone or tablet without requiring CasaOS.

## Architecture

- Existing React interface reused from `rpiammocan/virtual-bartender-casaos`
- Capacitor native Android container
- Android-local persistent data layer replacing the CasaOS `/api` backend
- Offline recipes, inventory, favorites, history, shopping list, Tonight's Bar, and matching

## Source snapshot

`source-pin.json` records the exact CasaOS source revision used as the UI starting point. Android builds do not automatically follow CasaOS `main`.

## Current phase

### Phase 1 — Android shell / APK build pipeline

The first workflow packages the pinned React frontend inside a native Android application and produces a debug APK. This is a build and UI smoke test.

### Phase 2 — Fully local Android data layer

The current React frontend talks to a FastAPI `/api` service. The Android edition will replace that network API boundary with an Android-local implementation so the final APK is genuinely standalone and offline.

## APK builds

GitHub Actions builds an installable debug APK with Gradle. Android's debug APK is automatically signed by the Android build tools and can be installed directly for testing.

Repository separation:

- CasaOS: `rpiammocan/virtual-bartender-casaos`
- Windows: `rpiammocan/virtual-bartender-windows`
- Android: `rpiammocan/virtual-bartender-android`
