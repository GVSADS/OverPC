ERROR=r"""<!DOCTYPE html>


<html dir="ltr" lang="zh">
	<head>
		<meta charset="utf-8">
		<meta name="theme-color" content="#fff">
		<meta name="viewport" content="width=device-width, initial-scale=1.0,
                                   maximum-scale=1.0, user-scalable=no">
		<title>127.0.0.1</title>
		<style>/* Copyright 2017 The Chromium Authors
   * Use of this source code is governed by a BSD-style license that can be
   * found in the LICENSE file. */
  
  a {
    color: var(--link-color);
  }
  
  body {
    --background-color: #fff;
    --error-code-color: var(--google-gray-700);
    --google-blue-100: rgb(210, 227, 252);
    --google-blue-300: rgb(138, 180, 248);
    --google-blue-600: rgb(26, 115, 232);
    --google-blue-700: rgb(25, 103, 210);
    --google-gray-100: rgb(241, 243, 244);
    --google-gray-300: rgb(218, 220, 224);
    --google-gray-500: rgb(154, 160, 166);
    --google-gray-50: rgb(248, 249, 250);
    --google-gray-600: rgb(128, 134, 139);
    --google-gray-700: rgb(95, 99, 104);
    --google-gray-800: rgb(60, 64, 67);
    --google-gray-900: rgb(32, 33, 36);
    --heading-color: var(--google-gray-900);
    --link-color: rgb(88, 88, 88);
    --popup-container-background-color: rgba(0,0,0,.65);
    --primary-button-fill-color-active: var(--google-blue-700);
    --primary-button-fill-color: var(--google-blue-600);
    --primary-button-text-color: #fff;
    --quiet-background-color: rgb(247, 247, 247);
    --secondary-button-border-color: var(--google-gray-500);
    --secondary-button-fill-color: #fff;
    --secondary-button-hover-border-color: var(--google-gray-600);
    --secondary-button-hover-fill-color: var(--google-gray-50);
    --secondary-button-text-color: var(--google-gray-700);
    --small-link-color: var(--google-gray-700);
    --text-color: var(--google-gray-700);
    --edge-background: var(--edge-grey-background);
    --edge-black: #101010;
    --edge-focus-color: #838383;
    --edge-blue-hover: #0078D4;
    --edge-blue-pressed: #1081D7;
    --edge-blue-rest: #0070C6;
    --edge-blue-selected: #004274;
    --edge-border-hover:#949494;
    --edge-border-pressed: #ADADAD;
    --edge-border-rest: #C5C5C5;
    --edge-grey-background: #F6F6F6;
    --edge-grey-selected: #C6C6C6;
    --edge-light-grey-hover: #F3F3F3;
    --edge-light-grey-pressed: #F7F7F7;
    --edge-light-grey-rest: #EFEFEF;
    --edge-primary-text-color: var(--edge-black);
    --edge-secondary-text-color: var(--edge-text-grey-rest);
    --edge-text-blue-hover: #0070C6;
    --edge-text-blue-rest: #0061AB;
    --edge-text-blue-pressed: #1081D7;
    --edge-text-grey-rest: #6F6F6F;
    --edge-white: #FFFFFF;
    --edge-primary-button-focus-shadow: 0 0 0 2px inset #F2F8FD;
    --edge-focus-outline: 2px solid var(--edge-focus-color);
    background: var(--edge-background);
    color: var(--edge-primary-text-color);
    word-wrap: break-word;
  }
  
  .nav-wrapper .secondary-button {
    background: var(--secondary-button-fill-color);
    border: 1px solid var(--secondary-button-border-color);
    color: var(--secondary-button-text-color);
    float: none;
    margin: 0;
    padding: 8px 16px;
  }
  
  .hidden {
    display: none;
  }
  
  html {
    -webkit-text-size-adjust: 100%;
    font-size: 125%;
  }
  
  .icon {
    background-repeat: no-repeat;
    background-size: 100%;
  }
  
  @media (prefers-color-scheme: dark) {
    body {
      --background-color: var(--google-gray-900);
      --error-code-color: var(--google-gray-500);
      --heading-color: var(--google-gray-500);
      --link-color: var(--google-blue-300);
      --primary-button-fill-color-active: rgb(129, 162, 208);
      --primary-button-fill-color: var(--google-blue-300);
      --primary-button-text-color: var(--google-gray-900);
      --quiet-background-color: var(--background-color);
      --secondary-button-border-color: var(--google-gray-700);
      --secondary-button-fill-color: var(--google-gray-900);
      --secondary-button-hover-fill-color: rgb(48, 51, 57);
      --secondary-button-text-color: var(--google-blue-300);
      --small-link-color: var(--google-blue-300);
      --text-color: var(--google-gray-500);
      --edge-black: #FFFFFF;
      --edge-focus-color: #888;
      --edge-blue-hover: #0070C6;
      --edge-blue-pressed: #0069B9;
      --edge-blue-rest: #0078D4;
      --edge-blue-selected: #63ACE5;
      --edge-border-hover:#909090;
      --edge-border-pressed: #787878;
      --edge-border-rest: #575757;
      --edge-grey-background: #2D2D2D;
      --edge-grey-selected: #676767;
      --edge-light-grey-hover: #424242;
      --edge-light-grey-pressed: #3E3E3E;
      --edge-light-grey-rest: #464646;
      --edge-text-blue-hover: #429BDF;
      --edge-text-blue-rest: #63ACE5;
      --edge-text-blue-pressed: #2189DA;
      --edge-text-grey-rest: #949494;
      --edge-white: #1D1D1D;
      --edge-primary-button-focus-shadow: 0 0 0 2px inset #F2F8FD;
    }
  }
  </style>
		<style>/* Copyright 2014 The Chromium Authors
     Copyright (C) Microsoft Corporation. All rights reserved.
     Use of this source code is governed by a BSD-style license that can be
     found in the LICENSE file. */
  
  button {
    border: 0;
    border-radius: 2px;
    box-sizing: border-box;
    color: var(--primary-button-text-color);
    cursor: pointer;
    float: right;
    font-size: .875em;
    margin: 0;
    padding: 8px 16px;
    transition: box-shadow 150ms cubic-bezier(0.4, 0, 0.2, 1);
    user-select: none;
  }
  
  [dir='rtl'] button {
    float: left;
  }
  
  .bad-clock button,
  .captive-portal button,
  .https-only button,
  .insecure-form button,
  .lookalike-url button,
  .main-frame-blocked button,
  .neterror button,
  .pdf button,
  .ssl button,
  .enterprise-block button,
  .enterprise-warn button,
  .safe-browsing-billing button {
    background: var(--edge-blue-rest);
  }
  
  .bad-clock a,
  .captive-portal a,
  .ssl a {
    color: var(--edge-text-blue-rest);
    text-decoration: none;
    border-bottom: 1px solid currentColor;
  }
  
  @media (forced-colors: active) {
    .bad-clock a,
    .captive-portal a,
    .lookalike-url a,
    .ssl a {
      -ms-high-contrast-adjust: none;
      color: LinkText;
      border-bottom: 1px solid currentColor;
    }
    .bad-clock a:focus,
    .captive-portal a:focus,
    .lookalike-url a:focus,
    .ssl a:focus {
      outline: none;
      border-bottom: 2px solid LinkText;
    }
  }
  
  
  .bad-clock #primary-button,
  .captive-portal #primary-button,
  .lookalike-url #primary-button,
  .ssl #primary-button {
    color: white;
    background-color: var(--edge-blue-rest);
    border: 2px solid var(--edge-blue-rest);
    font-family: system-ui, sans-serif;
    font-weight: 600;
    outline: none;
  }
  
  .bad-clock #primary-button:focus,
  .captive-portal #primary-button:focus,
  .lookalike-url #primary-button:focus,
  .ssl #primary-button:focus {
    border-color: var(--edge-focus-color);
    box-shadow: var(--edge-primary-button-focus-shadow);
  }
  
  .bad-clock #primary-button:hover,
  .captive-portal #primary-button:hover,
  .lookalike-url #primary-button:hover,
  .ssl #primary-button:hover {
    background-color: var(--edge-blue-hover);
    border-color: var(--edge-blue-hover);
  }
  
  .bad-clock #primary-button:active,
  .captive-portal #primary-button:active,
  .lookalike-url #primary-button:active,
  .ssl #primary-button:active {
    background-color: var(--edge-blue-pressed);
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3),
        0 2px 6px 2px rgba(60, 64, 67, .15);
  }
  
  @media(forced-colors: active) {
    /* Accent button */
    .bad-clock #primary-button,
    .captive-portal #primary-button,
    .lookalike-url #primary-button,
    .ssl #primary-button {
      -ms-high-contrast-adjust: none;
      background-color: Highlight;
      color: HighlightText;
      border: 2px solid transparent;
    }
    .bad-clock #primary-button:focus,
    .captive-portal #primary-button:focus,
    .lookalike-url #primary-button:focus,
    .ssl #primary-button:focus {
      outline: 2px solid ButtonText;
      border-color: transparent;
      box-shadow: none;
    }
    .bad-clock #primary-button:hover,
    .captive-portal #primary-button:hover,
    .lookalike-url #primary-button:hover,
    .ssl #primary-button:hover {
      background-color: HighlightText;
      color: Highlight;
      border: 2px solid Highlight;
    }
  }
  
  .bad-clock #details-button,
  .captive-portal #details-button,
  .lookalike-url #proceed-button,
  .ssl #details-button {
    color: var(--edge-primary-text-color);
    background-color: transparent;
    border-color: var(--edge-border-rest);
  }
  
  .bad-clock #details-button:focus,
  .captive-portal #details-button:focus,
  .lookalike-url #proceed-button:focus,
  .ssl #details-button:focus {
    outline: var(--edge-focus-outline);
  }
  
  .bad-clock #details-button:active,
  .captive-portal #details-button:active,
  .lookalike-url #proceed-button:active,
  .ssl #details-button:active {
    border-color: white;
    background: var(--edge-light-grey-pressed);
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3),
        0 2px 6px 2px rgba(60, 64, 67, .15);
  }
  
  .bad-clock #details-button:hover,
  .captive-portal #details-button:hover,
  .lookalike-url #proceed-button:hover,
  .ssl #details-button:hover {
    background: var(--edge-light-grey-hover);
    border-color: var(--edge-border-hover);
    text-decoration: none;
  }
  @media(forced-colors: active) {
    /* Outline button */
    .bad-clock #details-button,
    .captive-portal #details-button,
    .lookalike-url #proceed-button,
    .ssl #details-button {
      -ms-high-contrast-adjust: none;
      background-color: ButtonFace;
      color: ButtonText;
      border: 1px solid ButtonText;
    }
    .bad-clock #details-button:focus,
    .captive-portal #details-button:focus,
    .lookalike-url #proceed-button:focus,
    .ssl #details-button:focus {
      outline: 2px solid ButtonText;
    }
    .bad-clock #details-button:hover,
    .captive-portal #details-button:hover,
    .lookalike-url #proceed-button:hover,
    .ssl #details-button:hover {
      background-color: Highlight;
      color: HighlightText;
    }
  }
  
  .bad-clock #main-message > p,
  .captive-portal #main-message > p,
  .lookalike-url #main-message > p,
  .ssl #main-message > p {
    font-size: 14px;
    line-height: 20px;
    color: var(--edge-primary-text-color);
  }
  
  button:active {
    background: var(--primary-button-fill-color-active);
    outline: 0;
  }
  
  #debugging {
    display: inline;
    overflow: auto;
  }
  
  .debugging-content {
    line-height: 1em;
    margin-bottom: 0;
    margin-top: 1em;
  }
  
  .debugging-content-fixed-width {
    display: block;
    font-family: monospace;
    font-size: 1.2em;
    margin-top: 0.5em;
  }
  
  .debugging-title {
    font-weight: bold;
  }
  
  #details {
    margin: 0 0 50px;
  }
  
  #details p:not(:first-of-type) {
    margin-top: 20px;
  }
  
  .secondary-button:active {
    border-color: white;
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3),
        0 2px 6px 2px rgba(60, 64, 67, .15);
  }
  
  .secondary-button:hover {
    background: var(--secondary-button-hover-fill-color);
    border-color: var(--secondary-button-hover-border-color);
    text-decoration: none;
  }
  
  .error-code {
    color: var(--error-code-color);
    font-size: .8em;
    margin-top: 12px;
    text-transform: uppercase;
  }
  
  #error-debugging-info {
    font-size: 0.8em;
  }
  
  h1 {
    color: var(--edge-primary-text-color);
    font-size: 1.6em;
    font-weight: bold;
    line-height: 1.25em;
    margin-bottom: 16px;
  }
  
  h2 {
    font-size: 1.2em;
    font-weight: normal;
  }
  
  .icon {
    height: 72px;
    margin: 0 0 40px;
    width: 72px;
  }
  
  input[type=checkbox] {
    opacity: 0;
  }
  
  input[type=checkbox]:focus ~ .checkbox::after {
    outline: -webkit-focus-ring-color auto 5px;
  }
  
  .interstitial-wrapper {
    box-sizing: border-box;
    font-size: 1em;
    line-height: 1.6em;
    margin: 14vh auto 0;
    max-width: 600px;
    width: 100%;
  }
  
  #main-message > p {
    display: inline;
  }
  
  #extended-reporting-opt-in {
    font-size: .875em;
    margin-top: 32px;
  }
  
  #extended-reporting-opt-in label {
    display: grid;
    grid-template-columns: 1.8em 1fr;
    position: relative;
  }
  
  #enhanced-protection-message {
    border-radius: 20px;
    font-size: 1em;
    margin-top: 32px;
    padding: 10px 5px;
  }
  
  #enhanced-protection-message a {
    color: var(--google-red-10);
  }
  
  #enhanced-protection-message label {
    display: grid;
    grid-template-columns: 2.5em 1fr;
    position: relative;
  }
  
  #enhanced-protection-message div {
    margin: 0.5em;
  }
  
  #enhanced-protection-message .icon {
    height: 1.5em;
    vertical-align: middle;
    width: 1.5em;
  }
  
  #https-upgrades-message {
    border-radius: 4px;
    font-size: 1em;
  }
  
  .nav-wrapper {
    margin-top: 51px;
  }
  
  .nav-wrapper::after {
    clear: both;
    content: '';
    display: table;
    width: 100%;
  }
  
  .small-link {
    color: var(--small-link-color);
    font-size: .875em;
  }
  
  .checkboxes {
    flex: 0 0 24px;
  }
  
  .checkbox {
    --padding: .9em;
    background: transparent;
    display: block;
    height: 1em;
    left: -1em;
    padding-inline-start: var(--padding);
    position: absolute;
    right: 0;
    top: -.5em;
    width: 1em;
  }
  
  .checkbox::after {
    border: 1px solid white;
    border-radius: 2px;
    content: '';
    height: 1em;
    left: var(--padding);
    position: absolute;
    top: var(--padding);
    width: 1em;
  }
  
  .checkbox::before {
    background: transparent;
    border: 2px solid white;
    border-inline-end-width: 0;
    border-top-width: 0;
    content: '';
    height: .2em;
    left: calc(.3em + var(--padding));
    opacity: 0;
    position: absolute;
    top: calc(.3em  + var(--padding));
    transform: rotate(-45deg);
    width: .5em;
  }
  
  input[type=checkbox]:checked ~ .checkbox::before {
    opacity: 1;
  }
  
  #recurrent-error-message {
    background: var(--edge-light-grey-rest);
    border-radius: 4px;
    margin-bottom: 16px;
    margin-top: 12px;
    padding: 12px 16px;
  }
  
  .showing-recurrent-error-message #extended-reporting-opt-in {
    margin-top: 16px;
  }
  
  .showing-recurrent-error-message #enhanced-protection-message {
    margin-top: 16px;
  }
  
  @media (max-width: 700px) {
    .interstitial-wrapper {
      padding: 0 10%;
    }
  
    #error-debugging-info {
      overflow: auto;
    }
  }
  
  @media (max-width: 420px) {
    button,
    [dir='rtl'] button,
    .small-link {
      float: none;
      font-size: .825em;
      font-weight: 500;
      margin: 0;
      width: 100%;
    }
  
    button {
      padding: 16px 24px;
    }
  
    #details {
      margin: 20px 0 20px 0;
    }
  
    #details p:not(:first-of-type) {
      margin-top: 10px;
    }
  
    .secondary-button:not(.hidden) {
      display: block;
      margin-top: 20px;
      text-align: center;
      width: 100%;
    }
  
    .interstitial-wrapper {
      padding: 0 5%;
    }
  
    #extended-reporting-opt-in {
      margin-top: 24px;
    }
  
    #enhanced-protection-message {
      margin-top: 24px;
    }
  
    .nav-wrapper {
      margin-top: 30px;
    }
  }
  
  /**
   * Mobile specific styling.
   * Navigation buttons are anchored to the bottom of the screen.
   * Details message replaces the top content in its own scrollable area.
   */
  
  @media (max-width: 420px) {
    .nav-wrapper .secondary-button {
      border: 0;
      margin: 16px 0 0;
      margin-inline-end: 0;
      padding-bottom: 16px;
      padding-top: 16px;
    }
  }
  
  /* Fixed nav. */
  @media (min-width: 240px) and (max-width: 420px) and
         (min-height: 401px),
         (min-width: 421px) and (min-height: 240px) and
         (max-height: 560px) {
    body .nav-wrapper {
      background: var(--edge-grey-background);
      bottom: 0;
      box-shadow: 0 -22px 40px var(--edge-grey-background);
      left: 0;
      margin: 0 auto;
      max-width: 736px;
      padding-inline-end: 24px;
      padding-inline-start: 24px;
      position: fixed;
      right: 0;
      width: 100%;
      z-index: 2;
    }
  
    .interstitial-wrapper {
      max-width: 736px;
    }
  
    #details,
    #main-content {
      padding-bottom: 40px;
    }
  
    #details {
      padding-top: 5.5vh;
    }
  
    button.small-link {
      color: var(--google-blue-600);
    }
  }
  
  @media (max-width: 420px) and (orientation: portrait),
         (max-height: 560px) {
    body {
      margin: 0 auto;
    }
  
    button,
    #details-button,
    [dir='rtl'] button,
    button.small-link {
      font-size: .933em;
      margin: 6px 0;
      transform: translatez(0);
    }
  
    .nav-wrapper {
      box-sizing: border-box;
      padding-bottom: 8px;
      width: 100%;
    }
  
    #details {
      box-sizing: border-box;
      height: auto;
      margin: 0;
      opacity: 1;
      transition: opacity 250ms cubic-bezier(0.4, 0, 0.2, 1);
    }
  
    #details.hidden,
    #main-content.hidden {
      height: 0;
      opacity: 0;
      overflow: hidden;
      padding-bottom: 0;
      transition: none;
    }
  
    h1 {
      font-size: 1.5em;
      margin-bottom: 8px;
    }
  
    .icon {
      margin-bottom: 5.69vh;
    }
  
    .interstitial-wrapper {
      box-sizing: border-box;
      margin: 7vh auto 12px;
      padding: 0 24px;
      position: relative;
    }
  
    .interstitial-wrapper p {
      font-size: .95em;
      line-height: 1.61em;
      margin-top: 8px;
    }
  
    #main-content {
      margin: 0;
      transition: opacity 100ms cubic-bezier(0.4, 0, 0.2, 1);
    }
  
    .small-link {
      border: 0;
    }
  
    .suggested-left > #control-buttons,
    .suggested-right > #control-buttons {
      float: none;
      margin: 0;
    }
  }
  
  @media (min-width: 421px) and (min-height: 500px) and (max-height: 560px) {
    .interstitial-wrapper {
      margin-top: 10vh;
    }
  }
  
  @media (min-height: 400px) and (orientation:portrait) {
    .interstitial-wrapper {
      margin-bottom: 145px;
    }
  }
  
  @media (min-height: 299px) {
    .nav-wrapper {
      padding-bottom: 16px;
    }
  }
  
  @media (max-height: 560px) and (min-height: 240px) and (orientation:landscape) {
    .extended-reporting-has-checkbox #details {
      padding-bottom: 80px;
    }
  }
  
  @media (min-height: 500px) and (max-height: 650px) and (max-width: 414px) and
         (orientation: portrait) {
    .interstitial-wrapper {
      margin-top: 7vh;
    }
  }
  
  @media (min-height: 650px) and (max-width: 414px) and (orientation: portrait) {
    .interstitial-wrapper {
      margin-top: 10vh;
    }
  }
  
  /* Small mobile screens. No fixed nav. */
  @media (max-height: 400px) and (orientation: portrait),
         (max-height: 239px) and (orientation: landscape),
         (max-width: 419px) and (max-height: 399px) {
    .interstitial-wrapper {
      display: flex;
      flex-direction: column;
      margin-bottom: 0;
    }
  
    #details {
      flex: 1 1 auto;
      order: 0;
    }
  
    #main-content {
      flex: 1 1 auto;
      order: 0;
    }
  
    .nav-wrapper {
      flex: 0 1 auto;
      margin-top: 8px;
      order: 1;
      padding-inline-end: 0;
      padding-inline-start: 0;
      position: relative;
      width: 100%;
    }
  
    button,
    .nav-wrapper .secondary-button {
      padding: 16px 24px;
    }
  
    button.small-link {
      color: var(--google-blue-600);
    }
  }
  
  @media (max-width: 239px) and (orientation: portrait) {
    .nav-wrapper {
      padding-inline-end: 0;
      padding-inline-start: 0;
    }
  }
  
  </style>
		<style>/* Copyright 2013 The Chromium Authors. All rights reserved.
   * Copyright (C) Microsoft Corporation. All rights reserved.
   * Use of this source code is governed by a BSD-style license that can be
   * found in the LICENSE file. */
  
  /* Don't use the main frame div when the error is in a subframe. */
  body {
    background-color: var(--edge-grey-background);
  }
  
  html[subframe] #main-frame-error {
    display: none;
  }
  
  /* Don't use the subframe error div when the error is in a main frame. */
  html:not([subframe]) #sub-frame-error {
    display: none;
  }
  
  
  h1 {
    margin-top: 0;
    word-wrap: break-word;
    color: var(--edge-primary-text-color);
    margin-bottom: 22px;
  }
  
  h1 span {
    font-weight: 600;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-size: 32px;
    line-height: 40px;
  }
  
  h2 {
    color: var(--edge-secondary-text-color);
    font-size: 1.2em;
    font-weight: normal;
    margin: 10px 0;
  }
  
  a {
    color: var(--edge-text-blue-rest);
    text-decoration: none;
    border-bottom: 1px solid currentColor;
  }
  
  a:hover {
    color: var(--edge-text-blue-hover);
  }
  
  a:focus {
    outline: none;
    text-decoration: none;
    border-bottom: var(--edge-focus-outline);
  }
  
  #buttons {
    display: grid;
    grid-template-rows: auto auto;
  }
  
  .text-button {
    float: inline-start;
    margin-bottom: 10px;
  }
  
  #game-div {
    display: block;
  }
  
  #game-buttons {
    display: flex;
    align-items: center;
    margin-top: 26px;
  }
  
  #game-message {
    margin-inline-end: 6px;
  }
  
  #game-button {
    padding: 0;
    color: rgba(33, 105, 235, 1);
    background-color: transparent;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    display: inline-flex;
    gap: 6px;
  }
  
  #game-button:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }
  
  #game-button:focus:not(:disabled) {
    outline: var(--edge-focus-outline);
  }
  
  @media (forced-colors: active) {
    a:hover {
      color: HightlightText;
    }
  }
  
  
  .footer {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 1rem;
    display: flex;
  }
  
  .footer div:first-of-type {
    margin-right: auto;
  }
  
  .left-footer {
    display: flex;
    flex-direction: row;
    column-gap: 10px;
    margin-left: 40px;
  }
  
  .edge-logo {
    content: url(data:image/png;base64,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);
    width: 24px;
    height: 24px;
  }
  
  .edge-branding-text {
    flex: 82%;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 14px;
    line-height: 22px;
    text-align: right;
  }
  
  /* TODO(sayyagari): Migrate from usage of deprecated CSS -webkit-user-select. */
  .icon {
    -webkit-user-select: none;
    display: inline-block;
    width: 128px;
    height: 128px;
    margin: 0 0 20px;
  }
  
  .icon-generic {
    /* Can't access edge://theme/IDR_ERROR_NETWORK_GENERIC from an untrusted
     * renderer process, so embed the resource manually. */
    content: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABIAQMAAABvIyEEAAAABlBMVEUAAABTU1OoaSf/AAAAAXRSTlMAQObYZgAAADtJREFUKM9jYBgFRIP///8/wM16wGAhg5fF3ICbVYCfZf8fD4uBgXlAWPx/8LEKmJvxsCiwFxji/3GyANQXWAZOSFkcAAAAAElFTkSuQmCC) 1x,
        url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJAAAACQAQMAAADdiHD7AAAABlBMVEUAAABTU1OoaSf/AAAAAXRSTlMAQObYZgAAAFFJREFUSMdjYBgFo2AUjALSwX8weDCwQv+AmP2D/IFBIMRg3zCwQvYNQCGG+gEXAkXSwApBQP2o0CARqv//b8CFgHmF8c9ACw3lePwPAwMoBADzVzSl0RutTQAAAABJRU5ErkJggg==) 2x);
  }
  
  .icon-offline {
    content: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABIAQMAAABvIyEEAAAABlBMVEUAAABTU1OoaSf/AAAAAXRSTlMAQObYZgAAAGxJREFUeF7tyMEJwkAQRuFf5ipMKxYQiJ3Z2nSwrWwBA0+DQZcdxEOueaePp9+dQZFB7GpUcURSVU66yVNFj6LFICatThZB6r/ko/pbRpUgilY0Cbw5sNmb9txGXUKyuH7eV25x39DtJXUNPQGJtWFV+BT/QAAAAABJRU5ErkJggg==) 1x,
        url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJAAAACQBAMAAAAVaP+LAAAAGFBMVEUAAABTU1NNTU1TU1NPT09SUlJSUlJTU1O8B7DEAAAAB3RSTlMAoArVKvVgBuEdKgAAAJ1JREFUeF7t1TEOwyAMQNG0Q6/UE+RMXD9d/tC6womIFSL9P+MnAYOXeTIzMzMzMzMzaz8J9Ri6HoITmuHXhISE8nEh9yxDh55aCEUoTGbbQwjqHwIkRAEiIaG0+0AA9VBMaE89Rogeoww936MQrWdBr4GN/z0IAdQ6nQ/FIpRXDwHcA+JIJcQowQAlFUA0MfQpXLlVQfkzR4igS6ENjknm/wiaGhsAAAAASUVORK5CYII=) 2x);
    position: relative;
  }
  
  .icon-page-error {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTE0LjIxIDEzLjVsMS43NjcgMS43NzMtLjcwNC43MDRMMTMuNSAxNC4yMWwtMS43NzMgMS43NzMtLjcwNC0uNzEgMS43NzQtMS43NzQtMS43NzQtMS43NzMuNzA0LS43MDQgMS43NzMgMS43NzQgMS43NzMtMS43NzQuNzA0LjcxMUwxNC4yMSAxMy41ek0yIDE1aDh2MUgxVjBoOC43MUwxNCA0LjI5VjEwaC0xVjVIOVYxSDJ2MTR6bTgtMTFoMi4yOUwxMCAxLjcxVjR6IiBmaWxsPSIjMTAxMDEwIi8+PC9zdmc+);
  }
  
  .icon-thinking {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTMuNSAxMWExLjUwNSAxLjUwNSAwIDAxMS4zODMuOTE0Yy4wNzguMTgyLjExNy4zNzguMTE3LjU4NmExLjUwNSAxLjUwNSAwIDAxLS45MTQgMS4zODNBMS40NzIgMS40NzIgMCAwMTMuNSAxNGExLjUwNSAxLjUwNSAwIDAxLTEuMzgzLS45MTRBMS40NzEgMS40NzEgMCAwMTIgMTIuNWExLjUwNSAxLjUwNSAwIDAxLjkxNC0xLjM4M2MuMTgyLS4wNzguMzc4LS4xMTcuNTg2LS4xMTd6bTAgMmEuNDguNDggMCAwMC4zNTItLjE0OEEuNDguNDggMCAwMDQgMTIuNWEuNDguNDggMCAwMC0uMTQ4LS4zNTJBLjQ4LjQ4IDAgMDAzLjUgMTJhLjQ4LjQ4IDAgMDAtLjM1Mi4xNDhBLjQ4LjQ4IDAgMDAzIDEyLjVjMCAuMTM1LjA1LjI1My4xNDguMzUyQS40OC40OCAwIDAwMy41IDEzek0xIDE0YS45NDEuOTQxIDAgMDEuNzAzLjI5N0EuOTQxLjk0MSAwIDAxMiAxNWEuOTcuOTcgMCAwMS0uMDc4LjM5IDEuMDMgMS4wMyAwIDAxLS41MzEuNTMyQS45NjkuOTY5IDAgMDExIDE2YS45NjkuOTY5IDAgMDEtLjM5LS4wNzggMS4xMDMgMS4xMDMgMCAwMS0uMzItLjIxMSAxLjEwMyAxLjEwMyAwIDAxLS4yMTItLjMyQS45NjkuOTY5IDAgMDEwIDE1YS45NjkuOTY5IDAgMDEuMjktLjcwM0EuOTY5Ljk2OSAwIDAxMSAxNHpNMTEuNSAxYy42MiAwIDEuMjAzLjEyIDEuNzUuMzZhNC41MTUgNC41MTUgMCAwMTEuNDMuOTZjLjQwNi40MDcuNzI2Ljg4My45NiAxLjQzLjI0LjU0Ny4zNiAxLjEzLjM2IDEuNzUgMCAuNjItLjEyIDEuMjAzLS4zNiAxLjc1YTQuNTE2IDQuNTE2IDAgMDEtMi4zOSAyLjM5OEE0LjM5NSA0LjM5NSAwIDAxMTEuNSAxMGgtLjE4YTQuNDUyIDQuNDUyIDAgMDEtMi44MiAxYy0uMzggMC0uNzUtLjA0NC0xLjExLS4xMzNhNC43MzggNC43MzggMCAwMS0xLjAxNS0uMzk4IDQuNzM4IDQuNzM4IDAgMDEtLjg5LS42MjVBNC45MjQgNC45MjQgMCAwMTQuNzU3IDlINC41YTMuNDUgMy40NSAwIDAxLTEuMzY3LS4yNzMgMy41MzcgMy41MzcgMCAwMS0xLjg2LTEuODZBMy40NDYgMy40NDYgMCAwMTEgNS41YTMuNTEzIDMuNTEzIDAgMDEyLjEzMy0zLjIyN0EzLjQ0NiAzLjQ0NiAwIDAxNC41IDJoLjU0Yy4xNzYtLjMwNy4zOS0uNTgzLjY0LS44MjhBMy45NyAzLjk3IDAgMDE4LjUgMGMuNDkgMCAuOTYuMDg2IDEuNDE0LjI1OC40NTguMTcyLjg2Ny40MiAxLjIyNy43NDJoLjM1OXptMCA4YTMuMzkgMy4zOSAwIDAwMS4zNi0uMjczIDMuNTk2IDMuNTk2IDAgMDAxLjEwOS0uNzVBMy41MzIgMy41MzIgMCAwMDE1IDUuNWEzLjMxIDMuMzEgMCAwMC0uMjgxLTEuMzYgMy40MjIgMy40MjIgMCAwMC0uNzUtMS4xMDkgMy40MjMgMy40MjMgMCAwMC0xLjExLS43NUEzLjMxIDMuMzEgMCAwMDExLjUgMmgtLjc1OGEzLjk3NiAzLjk3NiAwIDAwLTEuMDIzLS43MzRDOS4zNjkgMS4wODkgOC45NjQgMSA4LjUgMWEyLjkgMi45IDAgMDAtLjk0NS4xNDhjLS4yODcuMDk0LS41NDcuMjMtLjc4Mi40MDdhMy4zMSAzLjMxIDAgMDAtLjYzMi42MzNBNC43ODUgNC43ODUgMCAwMDUuNjU2IDNINC41YTIuNTM1IDIuNTM1IDAgMDAtMS43NzMuNzQyIDIuNTA3IDIuNTA3IDAgMDAtLjUzMi43OWMtLjEzLjMtLjE5NS42MjMtLjE5NS45NjhzLjA2NS42Ny4xOTUuOTc3Yy4xMy4zMDIuMzA4LjU2Ny41MzIuNzk2LjIyOS4yMjQuNDk0LjQwMS43OTYuNTMyLjMwOC4xMy42MzMuMTk1Ljk3Ny4xOTVoLjgyOGMuMTYyLjMwMi4zNTIuNTc4LjU3LjgyOC4yMi4yNDUuNDY0LjQ1Ni43MzUuNjMzQTMuNDM2IDMuNDM2IDAgMDA4LjUgMTBhMy4zOSAzLjM5IDAgMDAxLjMyLS4yNTljLjQxMi0uMTc3Ljc5LS40MjQgMS4xMzMtLjc0MmguNTQ3eiIgZmlsbD0iIzEwMTAxMCIvPjwvc3ZnPg==);
  }
  
  .icon-blocked {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEyLjUgOWEzLjUxMyAzLjUxMyAwIDAxMi40NzcgMS4wMjMgMy41MTMgMy41MTMgMCAwMS43NSAzLjg0NCAzLjUxMyAzLjUxMyAwIDAxLTQuNTk0IDEuODYgMy41MzcgMy41MzcgMCAwMS0xLjg2LTEuODZBMy40NDYgMy40NDYgMCAwMTkgMTIuNWEzLjUxMyAzLjUxMyAwIDAxMi4xMzMtMy4yMjdBMy40NDYgMy40NDYgMCAwMTEyLjUgOXpNMTAgMTIuNWMwIC4zNDQuMDY1LjY3LjE5NS45NzcuMTMuMzAyLjMwOC41NjcuNTMyLjc5Ni4yMjkuMjI0LjQ5NC40MDIuNzk2LjUzMmEyLjU3OCAyLjU3OCAwIDAwMS42OTUuMDk0Yy4yMzUtLjA3My40NTQtLjE3OC42NTctLjMxM2wtMy40Ni0zLjQ2MWMtLjEzNi4yMDMtLjI0LjQyMi0uMzEzLjY1NkEyLjU3OCAyLjU3OCAwIDAwMTAgMTIuNXptNC41ODYgMS4zNzVjLjEzNS0uMjAzLjIzNy0uNDIyLjMwNS0uNjU2YTIuNDA3IDIuNDA3IDAgMDAtLjA5NC0xLjY4OCAyLjQ0MyAyLjQ0MyAwIDAwLS41NC0uNzg5IDIuNDQzIDIuNDQzIDAgMDAtLjc4OC0uNTM5IDIuNDA3IDIuNDA3IDAgMDAtMS42ODgtLjA5NGMtLjIzNC4wNjgtLjQ1My4xNy0uNjU2LjMwNWwzLjQ2IDMuNDYxek04LjQ2OSAxNWMuMjI0LjM3LjUuNzAzLjgyOCAxSDFWMGg4LjcxTDE0IDQuMjlWOGE0LjA3MyA0LjA3MyAwIDAwLTEtLjIxOVY1SDlWMUgydjE0aDYuNDY5ek0xMCA0aDIuMjlMMTAgMS43MVY0eiIgZmlsbD0iIzEwMTAxMCIvPjwvc3ZnPg==);
  }
  
  .icon-disconnected {
    content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDQ4IDIwNDgiIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZD0iTTE2MDAgMTE1MnE5MyAwIDE3NCAzNXQxNDMgOTYgOTYgMTQyIDM1IDE3NXEwIDkzLTM1IDE3NHQtOTYgMTQzLTE0MiA5Ni0xNzUgMzVxLTkzIDAtMTc0LTM1dC0xNDMtOTYtOTYtMTQyLTM1LTE3NXEwLTkzIDM1LTE3NHQ5Ni0xNDMgMTQyLTk2IDE3NS0zNXptLTMyMCA0NDhxMCA2NiAyNSAxMjR0NjggMTAyIDEwMiA2OSAxMjUgMjVxNDcgMCA5Mi0xM3Q4NC00MGwtNDQzLTQ0M3EtMjYgMzktMzkgODR0LTE0IDkyem01ODcgMTc2cTI2LTM5IDM5LTg0dDE0LTkycTAtNjYtMjUtMTI0dC02OS0xMDEtMTAyLTY5LTEyNC0yNnEtNDcgMC05MiAxM3QtODQgNDBsNDQzIDQ0M3ptLTc3NCAxMjVxMjIgMzYgNDggNjl0NTcgNjJxLTQzIDgtODYgMTJ0LTg4IDRxLTE0MSAwLTI3Mi0zNnQtMjQ0LTEwNC0yMDctMTYwLTE2MS0yMDctMTAzLTI0NS0zNy0yNzJxMC0xNDEgMzYtMjcydDEwNC0yNDQgMTYwLTIwNyAyMDctMTYxVDc1MiAzN3QyNzItMzdxMTQxIDAgMjcyIDM2dDI0NCAxMDQgMjA3IDE2MCAxNjEgMjA3IDEwMyAyNDUgMzcgMjcycTAgNDQtNCA4N3QtMTIgODdxLTU0LTU5LTExOC05OGw0LTM4cTItMTkgMi0zOCAwLTEzMC0zOC0yNTZoLTM2MnE4IDYyIDExIDEyM3Q1IDEyNHEtMzMgMy02NSAxMHQtNjQgMTh2LTM5cTAtNjAtNC0xMTh0LTEyLTExOEg2NTdxLTkgNjQtMTMgMTI3dC00IDEyOXEwIDY1IDQgMTI4dDEzIDEyOGg0NDZxLTM3IDU5LTYwIDEyOEg2NzlxOCAzNyAyMyA4OXQzNyAxMDkgNTEgMTEzIDY0IDEwMSA3OCA3MiA5MiAyOHExOCAwIDM1LTV0MzQtMTR6bTczOS0xMjYxcS0zOC04MS05MS0xNTJ0LTEyMC0xMzEtMTQzLTEwNC0xNjItNzVxMzYgNDkgNjQgMTA1dDUxIDExNSA0MCAxMjEgMjkgMTIxaDMzMnptLTgwOC01MTJxLTQ5IDAtOTEgMjd0LTc4IDczLTY1IDEwMS01MSAxMTMtMzcgMTA5LTIzIDg5aDY5MHEtOC0zNy0yMy04OXQtMzctMTA5LTUxLTExMy02NC0xMDEtNzgtNzItOTItMjh6bS0yOTIgNTBxLTg1IDI5LTE2MiA3NFQ0MjcgMzU3IDMwOCA0ODd0LTkyIDE1M2gzMzJxMTItNTkgMjgtMTIwdDM5LTEyMSA1Mi0xMTYgNjUtMTA1em0tNjA0IDg0NnEwIDEzMCAzOCAyNTZoMzYycS04LTY0LTEyLTEyN3QtNC0xMjlxMC02NSA0LTEyOHQxMi0xMjhIMTY2cS0zOCAxMjYtMzggMjU2em04OCAzODRxMzggODEgOTEgMTUydDEyMCAxMzEgMTQzIDEwNCAxNjIgNzVxLTM2LTQ5LTY1LTEwNXQtNTEtMTE1LTM5LTEyMS0yOS0xMjFIMjE2eiIgZmlsbD0iIzEwMTAxMCIvPjwvc3ZnPg==);
  }
  
  .icon-find {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTExIDBjLjIwOCAwIC40MTIuMDM0LjYxLjEwMi4xOTcuMDYyLjM4LjE1My41NDYuMjczLjE2Ny4xMi4zMTMuMjYzLjQzOC40My4xMy4xNjEuMjI5LjM0LjI5Ny41MzlsMi44MzYgOC41Yy4xODIuNTM2LjI3MyAxLjA4OC4yNzMgMS42NTYgMCAuNDg0LS4wOTQuOTQtLjI4MSAxLjM2N2EzLjUzNyAzLjUzNyAwIDAxLS43NSAxLjExIDMuNTk2IDMuNTk2IDAgMDEtMS4xMS43NUEzLjM5IDMuMzkgMCAwMTEyLjUgMTVjLS40NjMgMC0uOTEyLS4wODgtMS4zNDQtLjI2NmEzLjQ2NSAzLjQ2NSAwIDAxLTEuMTMzLS43NTcgMy40NjUgMy40NjUgMCAwMS0uNzU3LTEuMTMzQTMuNTEzIDMuNTEzIDAgMDE5IDExLjVWOEg3djMuNWEzLjQ4OCAzLjQ4OCAwIDAxLTIuMTY0IDMuMjM0QTMuNDU0IDMuNDU0IDAgMDEzLjUgMTVhMy40NSAzLjQ1IDAgMDEtMS4zNjctLjI3MyAzLjcyMiAzLjcyMiAwIDAxLTEuMTEtLjc1IDMuNzIyIDMuNzIyIDAgMDEtLjc1LTEuMTFBMy40NDYgMy40NDYgMCAwMTAgMTEuNWMwLS41NjguMDkxLTEuMTIuMjczLTEuNjU2LjAyNi0uMDczLjA4Ni0uMjUuMTgtLjUzMWwuMzQ0LTEuMDQ3Yy4xNC0uNDE3LjI5NC0uODc1LjQ2LTEuMzc1YTUxNi4yMDYgNTE2LjIwNiAwIDAwMS4wMTYtMy4wMjRsLjQzLTEuMjk3Yy4xMjUtLjM3NS4yMjQtLjY3Ny4yOTctLjkwNmwuMTE3LS4zNDRjLjA3OC0uMTkyLjE4LS4zNy4zMDUtLjUzLjEyNS0uMTY4LjI2OC0uMzA4LjQzLS40MjMuMTY2LS4xMTQuMzQ2LS4yMDMuNTM5LS4yNjVBMS44MSAxLjgxIDAgMDE1IDBjLjM4NSAwIC43LjA2My45NDUuMTg4LjI1LjEyNC40NDguMjk0LjU5NC41MDcuMTUxLjIwOS4yNi40NS4zMjguNzI3LjA2OC4yNy4xMS41NTUuMTI1Ljg1MS4wMjEuMjk3LjAyNi41OTcuMDE2Ljg5OUM3LjAwMyAzLjQ2OSA3IDMuNzQ1IDcgNGgyYzAtLjI1NS0uMDA1LS41MzEtLjAxNi0uODI4LS4wMDUtLjMwMiAwLS42MDIuMDE2LS44OTkuMDItLjI5Ni4wNjUtLjU4LjEzMy0uODUxLjA2OC0uMjc2LjE3NC0uNTE4LjMyLS43MjdhMS42MSAxLjYxIDAgMDEuNTk0LS41MDdDMTAuMjk3LjA2MSAxMC42MTUgMCAxMSAwek0zLjUgMTRjLjM0NCAwIC42NjctLjA2NS45NjktLjE5NS4zMDItLjEzNi41NjUtLjMxNS43ODktLjU0YTIuNTMgMi41MyAwIDAwLjUzOS0uNzk2Yy4xMzUtLjMwMi4yMDMtLjYyNS4yMDMtLjk2OXMtLjA2OC0uNjY3LS4yMDMtLjk2OWEyLjQ0NCAyLjQ0NCAwIDAwLS41NC0uNzg5IDIuNDQ0IDIuNDQ0IDAgMDAtLjc4OC0uNTM5QTIuMzQxIDIuMzQxIDAgMDAzLjUgOWMtLjM0NCAwLS42NjcuMDY4LS45NjkuMjAzLS4zMDIuMTMtLjU2Ny4zMS0uNzk3LjU0YTIuNjIgMi42MiAwIDAwLS41MzkuNzg4Yy0uMTMuMzAyLS4xOTUuNjI1LS4xOTUuOTY5cy4wNjUuNjY3LjE5NS45NjljLjEzNi4zMDIuMzE1LjU2OC41NC43OTcuMjI5LjIyNC40OTQuNDAzLjc5Ni41MzkuMzAyLjEzLjYyNS4xOTUuOTY5LjE5NXpNNiAyYS45NDEuOTQxIDAgMDAtLjI5Ny0uNzAzQS45NDEuOTQxIDAgMDA1IDFjLS4yMDMgMC0uMzk2LjA2My0uNTc4LjE4OGEuOTYzLjk2MyAwIDAwLS4zNjcuNDg0TDEuNzk3IDguNDM4Yy4yNjYtLjE0MS41NDItLjI0OC44MjgtLjMyQTMuMzEgMy4zMSAwIDAxMy41IDhjLjE3MiAwIC4zOC4wMjYuNjI1LjA3OC4yNS4wNDcuNDk3LjExNy43NDIuMjExLjI1LjA4OS40NzcuMTk4LjY4LjMyOC4yMDguMTMuMzYuMjc2LjQ1My40MzhWMnptMyA1VjVIN3YyaDJ6bTEgMi4wNTVjLjA5NC0uMTYyLjI0Mi0uMzA4LjQ0NS0uNDM4LjIwOS0uMTMuNDM1LS4yNC42OC0uMzI4YTQuNDMgNC40MyAwIDAxLjc0Mi0uMjFjLjI1LS4wNTMuNDYxLS4wNzkuNjMzLS4wNzkuMjk3IDAgLjU4OC4wNC44NzUuMTE3LjI4Ny4wNzMuNTYzLjE4LjgyOC4zMmwtMi4yNTgtNi43NjVhLjk1Ljk1IDAgMDAtLjM3NS0uNDg0Ljk3Ljk3IDAgMDAtLjk2LS4xMSAxLjAzIDEuMDMgMCAwMC0uNTMyLjUzMUEuOTY5Ljk2OSAwIDAwMTAgMnY3LjA1NXpNMTIuNSAxNGMuMzQ0IDAgLjY2Ny0uMDY1Ljk2OS0uMTk1LjMwMi0uMTM2LjU2NS0uMzE1Ljc4OS0uNTRhMi41MyAyLjUzIDAgMDAuNTM5LS43OTZjLjEzNS0uMzAyLjIwMy0uNjI1LjIwMy0uOTY5cy0uMDY4LS42NjctLjIwMy0uOTY5YTIuNDQ0IDIuNDQ0IDAgMDAtLjU0LS43ODkgMi40NDQgMi40NDQgMCAwMC0uNzg4LS41MzlBMi4zNDEgMi4zNDEgMCAwMDEyLjUgOWMtLjM0NCAwLS42NjcuMDY4LS45NjkuMjAzYTIuNTIgMi41MiAwIDAwLS43OTcuNTQgMi42MiAyLjYyIDAgMDAtLjUzOS43ODhjLS4xMy4zMDItLjE5NS42MjUtLjE5NS45NjlzLjA2NS42NjcuMTk1Ljk2OWMuMTM2LjMwMi4zMTUuNTY4LjU0Ljc5Ny4yMjkuMjI0LjQ5NC40MDMuNzk2LjUzOS4zMDIuMTMuNjI1LjE5NS45NjkuMTk1eiIgZmlsbD0iIzEwMTAxMCIvPjwvc3ZnPg==);
  }
  
  .icon-insecure-site {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTE0IDd2OUgyVjdoOVY0YzAtLjQyNy0uMDc4LS44MjMtLjIzNC0xLjE4OGEyLjgxOSAyLjgxOSAwIDAwLS42MzMtLjk0NSAyLjgxOSAyLjgxOSAwIDAwLS45NDUtLjYzM0EyLjk4MiAyLjk4MiAwIDAwOCAxYy0uNDI3IDAtLjgyMy4wNzgtMS4xODguMjM0YTIuOTA1IDIuOTA1IDAgMDAtMS41ODUgMS41NzlBMy4wNjEgMy4wNjEgMCAwMDUgNEg0YzAtLjU2OC4xMDItMS4wOTQuMzA1LTEuNTc4LjIwMy0uNDkuNDg0LS45MTQuODQzLTEuMjc0QTMuOTIgMy45MiAwIDAxNi40MTQuMzA1IDQuMDk3IDQuMDk3IDAgMDE4IDBhNC4wNCA0LjA0IDAgMDExLjU3OC4zMDVjLjQ5LjIwMy45MTQuNDg0IDEuMjc0Ljg0My4zNTkuMzYuNjQuNzg0Ljg0MyAxLjI3NEE0LjA0IDQuMDQgMCAwMTEyIDR2M2gyem0tMSAxSDN2N2gxMFY4eiIgZmlsbD0iIzEwMTAxMCIvPjwvc3ZnPg==);
  }
  
  .icon-page-briefcase {
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yNC4wNTUgNjBhOC45NDggOC45NDggMCAwMDEuNDYgNEg0VjBoMzQuODQ0TDU2IDE3LjE1NnYxMi4wOTlBNi45NjggNi45NjggMCAwMDUyIDI4di04SDM2VjRIOHY1NmgxNi4wNTV6bTI1LjEwMS00NEg0MFY2Ljg0NEw0OS4xNTYgMTZ6IiBmaWxsPSIjMTAxMDEwIi8+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zNyAzOHYtM2EzIDMgMCAwMTMtM2gxMmEzIDMgMCAwMTMgM3YzaDRhNSA1IDAgMDE1IDV2MTZhNSA1IDAgMDEtNSA1SDMzYTUgNSAwIDAxLTUtNVY0M2E1IDUgMCAwMTUtNWg0em00IDB2LTJoMTB2Mkg0MXptLTggNGExIDEgMCAwMC0xIDF2M2EzIDMgMCAwMDMgM2g4di0xYTEgMSAwIDAxMS0xaDRhMSAxIDAgMDExIDF2MWg4YTMgMyAwIDAwMy0zdi0zYTEgMSAwIDAwLTEtMUgzM3ptMiAxMWg4djFhMSAxIDAgMDAxIDFoNGExIDEgMCAwMDEtMXYtMWg4YzEuMDc0IDAgMi4wOS0uMjQyIDMtLjY3NFY1OWExIDEgMCAwMS0xIDFIMzNhMSAxIDAgMDEtMS0xdi02LjY3NGMuOTEuNDMyIDEuOTI2LjY3NCAzIC42NzR6IiBmaWxsPSIjMTAxMDEwIi8+PC9zdmc+);
  }
  
  .icon-elixir-page-error {
    content: url(data:image/webp;base64,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);
  }
  
  .icon-elixir-thinking {
    content: url(data:image/webp;base64,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);
  }
  
  .icon-elixir-blocked {
    content: url(data:image/webp;base64,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);
  }
  
  .icon-elixir-disconnected {
    content: url(data:image/webp;base64,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);
  }
  
  .icon-elixir-insecure {
    content: url(data:image/webp;base64,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);
  }
  
  .icon-play-game-button {
    width: 20px;
    height: 20px;
    content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xNSA0LjVDMTUuMjA4NCA0LjUgMTUuMzk1IDQuNjI5MjggMTUuNDY4MiA0LjgyNDQzQzE1LjkwODIgNS45OTc4NiAxNi43NDM4IDYuNDk5ODkgMTcuNSA2LjQ5OTg5QzE3Ljc3NjEgNi40OTk4OSAxOCA2LjcyMzc1IDE4IDYuOTk5ODlDMTggNy4yNzYwNCAxNy43NzYxIDcuNDk5ODkgMTcuNSA3LjQ5OTg5QzE2LjUzODMgNy40OTk4OSAxNS42MjQxIDcuMDAyOTcgMTUgNi4wODczOUMxNC4zNzU5IDcuMDAyOTcgMTMuNDYxNyA3LjQ5OTkgMTIuNSA3LjQ5OTk1QzExLjUzODQgNy41IDEwLjYyNDEgNy4wMDMxNSAxMCA2LjA4NzY4QzkuMzc1OTEgNy4wMDMxNSA4LjQ2MTY0IDcuNSA3LjUgNy41QzYuNTM4NTQgNy41IDUuNjI0NDMgNy4wMDMzNCA1LjAwMDM1IDYuMDg4MTlDNC4zNzYzNiA3LjAwNDgzIDMuNDYyMDIgNy41MDI1NCAyLjUwMDAxIDcuNTAyNTVDMi4yMjM4NyA3LjUwMjU2IDIgNy4yNzg3IDIgNy4wMDI1NkMyIDYuNzI2NDIgMi4yMjM4NSA2LjUwMjU2IDIuNDk5OTkgNi41MDI1NUMzLjI1NTkgNi41MDI1NCA0LjA5MTYgNi4wMDAxMSA0LjUzMTc3IDQuODI1MDNDNC42MDQ4OSA0LjYyOTgzIDQuNzkxNDQgNC41MDA0NyA0Ljk5OTg5IDQuNTAwNDJDNS4yMDgzNCA0LjUwMDM4IDUuMzk0OTUgNC42Mjk2NiA1LjQ2ODE1IDQuODI0ODNDNS45MDgxOSA1Ljk5ODAxIDYuNzQzNzEgNi41IDcuNSA2LjVDOC4yNTYyOSA2LjUgOS4wOTE4MSA1Ljk5ODAxIDkuNTMxODUgNC44MjQ4M0M5LjYwNTA0IDQuNjI5NjkgOS43OTE1OSA0LjUwMDQyIDEwIDQuNTAwNDJDMTAuMjA4NCA0LjUwMDQyIDEwLjM5NSA0LjYyOTY5IDEwLjQ2ODIgNC44MjQ4M0MxMC45MDgyIDUuOTk4MDIgMTEuNzQzNyA2LjQ5OTk5IDEyLjUgNi40OTk5NUMxMy4yNTYyIDYuNDk5OTEgMTQuMDkxOCA1Ljk5Nzg1IDE0LjUzMTggNC44MjQ0M0MxNC42MDUgNC42MjkyOCAxNC43OTE2IDQuNSAxNSA0LjVaTTE1IDkuNUMxNS4yMDg0IDkuNSAxNS4zOTUgOS42MjkyOCAxNS40NjgyIDkuODI0NDNDMTUuOTA4MiAxMC45OTc5IDE2Ljc0MzggMTEuNDk5OSAxNy41IDExLjQ5OTlDMTcuNzc2MSAxMS40OTk5IDE4IDExLjcyMzggMTggMTEuOTk5OUMxOCAxMi4yNzYgMTcuNzc2MSAxMi40OTk5IDE3LjUgMTIuNDk5OUMxNi41MzgzIDEyLjQ5OTkgMTUuNjI0MSAxMi4wMDMgMTUgMTEuMDg3NEMxNC4zNzU5IDEyLjAwMyAxMy40NjE3IDEyLjQ5OTkgMTIuNSAxMi40OTk5QzExLjUzODQgMTIuNSAxMC42MjQxIDEyLjAwMzIgMTAgMTEuMDg3N0M5LjM3NTkxIDEyLjAwMzIgOC40NjE2NCAxMi41IDcuNSAxMi41QzYuNTM4NTQgMTIuNSA1LjYyNDQzIDEyLjAwMzMgNS4wMDAzNSAxMS4wODgyQzQuMzc2MzYgMTIuMDA0OCAzLjQ2MjAyIDEyLjUwMjUgMi41MDAwMSAxMi41MDI2QzIuMjIzODcgMTIuNTAyNiAyIDEyLjI3ODcgMiAxMi4wMDI2QzIgMTEuNzI2NCAyLjIyMzg1IDExLjUwMjYgMi40OTk5OSAxMS41MDI2QzMuMjU1OSAxMS41MDI1IDQuMDkxNiAxMS4wMDAxIDQuNTMxNzcgOS44MjUwM0M0LjYwNDg5IDkuNjI5ODMgNC43OTE0NCA5LjUwMDQ3IDQuOTk5ODkgOS41MDA0MkM1LjIwODM0IDkuNTAwMzggNS4zOTQ5NSA5LjYyOTY2IDUuNDY4MTUgOS44MjQ4M0M1LjkwODE5IDEwLjk5OCA2Ljc0MzcxIDExLjUgNy41IDExLjVDOC4yNTYyOSAxMS41IDkuMDkxODEgMTAuOTk4IDkuNTMxODUgOS44MjQ4M0M5LjYwNTA0IDkuNjI5NjkgOS43OTE1OSA5LjUwMDQyIDEwIDkuNTAwNDJDMTAuMjA4NCA5LjUwMDQyIDEwLjM5NSA5LjYyOTY5IDEwLjQ2ODIgOS44MjQ4M0MxMC45MDgyIDEwLjk5OCAxMS43NDM3IDExLjUgMTIuNSAxMS40OTk5QzEzLjI1NjIgMTEuNDk5OSAxNC4wOTE4IDEwLjk5NzkgMTQuNTMxOCA5LjgyNDQzQzE0LjYwNSA5LjYyOTI4IDE0Ljc5MTYgOS41IDE1IDkuNVpNMTUuNDY4MiAxNC44MjQ0QzE1LjM5NSAxNC42MjkzIDE1LjIwODQgMTQuNSAxNSAxNC41QzE0Ljc5MTYgMTQuNSAxNC42MDUgMTQuNjI5MyAxNC41MzE4IDE0LjgyNDRDMTQuMDkxOCAxNS45OTc5IDEzLjI1NjIgMTYuNDk5OSAxMi41IDE2LjQ5OTlDMTEuNzQzNyAxNi41IDEwLjkwODIgMTUuOTk4IDEwLjQ2ODIgMTQuODI0OEMxMC4zOTUgMTQuNjI5NyAxMC4yMDg0IDE0LjUwMDQgMTAgMTQuNTAwNEM5Ljc5MTU5IDE0LjUwMDQgOS42MDUwNCAxNC42Mjk3IDkuNTMxODUgMTQuODI0OEM5LjA5MTgxIDE1Ljk5OCA4LjI1NjI5IDE2LjUgNy41IDE2LjVDNi43NDM3MSAxNi41IDUuOTA4MTkgMTUuOTk4IDUuNDY4MTUgMTQuODI0OEM1LjM5NDk1IDE0LjYyOTcgNS4yMDgzNCAxNC41MDA0IDQuOTk5ODkgMTQuNTAwNEM0Ljc5MTQ0IDE0LjUwMDUgNC42MDQ4OSAxNC42Mjk4IDQuNTMxNzcgMTQuODI1QzQuMDkxNiAxNi4wMDAxIDMuMjU1OSAxNi41MDI1IDIuNDk5OTkgMTYuNTAyNkMyLjIyMzg1IDE2LjUwMjYgMiAxNi43MjY0IDIgMTcuMDAyNkMyIDE3LjI3ODcgMi4yMjM4NyAxNy41MDI2IDIuNTAwMDEgMTcuNTAyNkMzLjQ2MjAyIDE3LjUwMjUgNC4zNzYzNiAxNy4wMDQ4IDUuMDAwMzUgMTYuMDg4MkM1LjYyNDQzIDE3LjAwMzMgNi41Mzg1NCAxNy41IDcuNSAxNy41QzguNDYxNjQgMTcuNSA5LjM3NTkxIDE3LjAwMzIgMTAgMTYuMDg3N0MxMC42MjQxIDE3LjAwMzIgMTEuNTM4NCAxNy41IDEyLjUgMTcuNDk5OUMxMy40NjE3IDE3LjQ5OTkgMTQuMzc1OSAxNy4wMDMgMTUgMTYuMDg3NEMxNS42MjQxIDE3LjAwMyAxNi41MzgzIDE3LjQ5OTkgMTcuNSAxNy40OTk5QzE3Ljc3NjEgMTcuNDk5OSAxOCAxNy4yNzYgMTggMTYuOTk5OUMxOCAxNi43MjM4IDE3Ljc3NjEgMTYuNDk5OSAxNy41IDE2LjQ5OTlDMTYuNzQzOCAxNi40OTk5IDE1LjkwODIgMTUuOTk3OSAxNS40NjgyIDE0LjgyNDRaIiBmaWxsPSIjMjE2OUVCIi8+DQo8L3N2Zz4NCg==);
  }
  
  .icon-disabled {
    content: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABICAMAAAAZF4G5AAAABlBMVEVMaXFTU1OXUj8tAAAAAXRSTlMAQObYZgAAASZJREFUeAHd11Fq7jAMRGGf/W/6PoWB67YMqv5DybwG/CFjRuR8JBw3+ByiRjgV9W/TJ31P0tBfC6+cj1haUFXKHmVJo5wP98WwQ0ZCbfUc6LQ6VuUBz31ikADkLMkDrfUC4rR6QGW+gF6rx7NaHWCj1Y/W6lf4L7utvgBSt3rBFSS/XBMPUILcJINHCBWYUfpWn4NBi1ZfudIc3rf6/NGEvEA+AsYTJozmXemjXeLZAov+mnkN2HfzXpMSVQDnGw++57qNJ4D1xitA2sJ+VAWMygSEaYf2mYPTjZfk2K8wmP7HLIH5Mg4/pP+PEcDzUvDMvYbs/2NWwPO5vBdMZE4EE5UTQLiBFDaUlTDPBRoJ9HdAYIkIo06og3BNXtCzy7zA1aXk5x+tJARq63eAygAAAABJRU5ErkJggg==) 1x,
        url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAACQAQMAAAArwfVjAAAABlBMVEVMaXFTU1OXUj8tAAAAAXRSTlMAQObYZgAAAYdJREFUeF7F1EFqwzAUBNARAmVj0FZe5QoBH6BX+dn4GlY2PYNzGx/A0CvkCIJuvIraKJKbgBvzf2g62weDGD7CYggpfFReis4J0ey9EGFIiEQQojFSlA9kSIiqd0KkFjKsewgRbStEN19mxUPTtmW9HQ/h6tyqNQ8NlSMZdzyE6qkoE0trVYGFm0n1WYeBhduzwbwBC7voS+vIxfeMjeaiLxsMMtQNwMPtuew+DjzcTHk8YMfDknEcIUOtf2lVfgVH3K4Xv5PRYAXRVMtItIJ3rfaCIVn9DsTH2NxisAVRex2Hh3hX+/mRUR08bAwPEYsI51ZxWH4Q0SpicQRXeyEaIug48FEdegARfMz/tADVsRciwTAxW308ehmC2gLraC+YCbV3QoTZexa+zegAEW5PhhgYfmbvJgcRqngGByOSXdFJcLk2JeDPEN0kxe1JhIt5FiFA+w+ItMELsUyPF2IaJ4aILqb4FbxPwhImwj6JauKgDUCYaxmYIsd4KXdMjIC9ItB5Bn4BNRwsG0XM2nwAAAAASUVORK5CYII=) 2x);
    width: 112px;
  }
  
  .managed-icon {
    content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDQ4IDIwNDgiIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiI+PHBhdGggZD0iTTIwNDggNTQ0djEwODhxMCAzMy0xMiA2MnQtMzUgNTEtNTEgMzQtNjIgMTNIMTYwcS0zMyAwLTYyLTEydC01MS0zNS0zNC01MS0xMy02MlY1NDRxMC0zMyAxMi02MnQzNS01MSA1MS0zNCA2Mi0xM2g0ODBWMjM2cTAtMjIgOC00MnQyMy0zNCAzNC0yMyA0My05aDU1MnEyMiAwIDQyIDh0MzQgMjMgMjMgMzUgOSA0MnYxNDhoNDgwcTMzIDAgNjIgMTJ0NTEgMzUgMzQgNTEgMTMgNjJ6TTc0OCAyMzZ2MTQ4aDU1MlYyMzZINzQ4em0xMTQwIDE0MjhxMTQgMCAyMy05dDktMjN2LTUxNHEtNjAgMzQtMTI4IDM0aC02NDB2ODNxMCAxOS0xMyAzMnQtMzIgMTNIOTQxcS0xOSAwLTMyLTEzdC0xMy0zMnYtODNIMjU2cS02OCAwLTEyOC0zNHY1MTRxMCAxNCA5IDIzdDIzIDloMTcyOHptLTk2LTY0MHEyNyAwIDUwLTEwdDQwLTI3IDI4LTQxIDEwLTUwVjU0NHEwLTE0LTktMjN0LTIzLTlIMTYwcS0xNCAwLTIzIDl0LTkgMjN2MzUycTAgMjcgMTAgNTB0MjcgNDAgNDEgMjggNTAgMTBoNjQwdi04M3EwLTE5IDEzLTMydDMyLTEzaDE2NnExOSAwIDMyIDEzdDEzIDMydjgzaDY0MHoiLz48L3N2Zz4=);
    margin-inline-end: 6px;
    height: 16px;
    width: 16px;
  }
  
  .error-code {
    display: block;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-size: 10px;
    line-height: 14px;
    color: var(--edge-secondary-text-color);
    margin-top: 20px;
    font-weight: 400;
  }
  
  #content-top {
    margin: 20px;
  }
  
  .hidden {
    display: none !important;
  }
  
  #suggestion {
    margin-top: 15px;
  }
  
  #suggestions-list p {
    margin-block-end: 0;
    color: var(--edge-primary-text-color);
    font-weight: 700;
  }
  
  #suggestions-list ul {
    margin-top: 0;
    margin-left: 10px;
    color: var(--edge-primary-text-color);
    padding-inline-start: 0;
    list-style: none;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
  }
  
  #suggestions-list li {
    margin-top: 12px;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
  }
  
  #suggestions-list li:before {
    content: "•";
    font-size: 14px;
    padding-right: 1em;
  }
  
  .single-suggestion li:before {
    display: none;
  }
  
  #short-suggestion {
    margin-top: 5px;
  }
  
  #error-information-button {
    content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSJub25lIiBkPSJNMCAwaDI0djI0SDB6Ii8+PHBhdGggZD0iTTExIDE4aDJ2LTJoLTJ2MnptMS0xNkM2LjQ4IDIgMiA2LjQ4IDIgMTJzNC40OCAxMCAxMCAxMCAxMC00LjQ4IDEwLTEwUzE3LjUyIDIgMTIgMnptMCAxOGMtNC40MSAwLTgtMy41OS04LThzMy41OS04IDgtOCA4IDMuNTkgOCA4LTMuNTkgOC04IDh6bTAtMTRjLTIuMjEgMC00IDEuNzktNCA0aDJjMC0xLjEuOS0yIDItMnMyIC45IDIgMmMwIDItMyAxLjc1LTMgNWgyYzAtMi4yNSAzLTIuNSAzLTUgMC0yLjIxLTEuNzktNC00LTR6Ii8+PC9zdmc+);
    height: 24px;
    vertical-align: -.15em;
    width: 24px;
  }
  
  .use-popup-container#error-information-popup-container #error-information-popup {
    align-items: center;
    background-color: var(--edge-grey-background);
    display: flex;
    height: 100%;
    left: 0;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 100;
  }
  
  .use-popup-container#error-information-popup-container #error-information-popup-content>p {
    margin-bottom: 11px;
    margin-inline-start: 20px;
  }
  
  #error-information-popup-content {
    margin-top: 20px;
  }
  
  .use-popup-container#error-information-popup-container #suggestions-list ul {
    margin-inline-start: 15px;
  }
  
  .use-popup-container#error-information-popup-container #error-information-popup-box {
    background-color: var(--edge-white);
    left: 5%;
    padding-bottom: 15px;
    padding-top: 15px;
    position: fixed;
    width: 90%;
    z-index: 101;
  }
  
  .use-popup-container#error-information-popup-container div.error-code {
    margin-inline-start: 20px;
  }
  
  .use-popup-container#error-information-popup-container #suggestions-list p {
    margin-inline-start: 20px;
  }
  
  :not(.use-popup-container)#error-information-popup-container #error-information-popup-close {
    display: none;
  }
  
  #error-information-popup-close {
    margin-bottom: 0px;
    margin-inline-end: 35px;
    margin-top: 15px;
    text-align: end;
  }
  
  .link-button {
    color: var(--edge-text-blue-rest);
    display: inline-block;
    font-weight: bold;
    text-transform: uppercase;
  }
  
  #sub-frame-error-details {
    color: var(--edge-secondary-text-color);
    
  }
  
  [jscontent=hostName],
  [jscontent=failedUrl] {
    overflow-wrap: break-word;
  }
  
  #search-container {
    /* Prevents a space between controls. */
    display: flex;
    margin-top: 20px;
  }
  
  .snackbar {
    background: #323232;
    border-radius: 2px;
    bottom: 24px;
    box-sizing: border-box;
    color: #fff;
    font-size: .87em;
    left: 24px;
    max-width: 568px;
    min-width: 288px;
    opacity: 0;
    padding: 16px 24px 12px;
    position: fixed;
    transform: translateY(90px);
    will-change: opacity, transform;
    z-index: 999;
  }
  
  .snackbar-show {
    -webkit-animation:
      show-snackbar .25s cubic-bezier(0.0, 0.0, 0.2, 1) forwards,
      hide-snackbar .25s cubic-bezier(0.4, 0.0, 1, 1) forwards 5s;
  }
  
  @-webkit-keyframes show-snackbar {
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @-webkit-keyframes hide-snackbar {
    0% {
      opacity: 1;
      transform: translateY(0);
    }
  
    100% {
      opacity: 0;
      transform: translateY(90px);
    }
  }
  
  .suggestions {
    margin-top: 18px;
    color: var(--edge-primary-text-color);
    font-size: 14px;
    line-height: 20px;
  }
  
  .suggestion-header {
    font-weight: bold;
    margin-bottom: 4px;
  }
  
  /* Decrease padding at low sizes. */
  @media (max-width: 640px),
  (max-height: 640px) {
    h1 {
      margin: 0 0 15px;
    }
  
    #content-top {
      margin: 15px;
    }
  
    .suggestions {
      margin-top: 10px;
    }
  
    .suggestion-header {
      margin-bottom: 0;
    }
  }
  
  #download-link,
  #download-link-clicked {
    margin-bottom: 30px;
    margin-top: 30px;
  }
  
  #download-link-clicked {
    color: #BBB;
  }
  
  #download-link:before,
  #download-link-clicked:before {
    content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxLjJlbSIgaGVpZ2h0PSIxLjJlbSIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNNSAyMGgxNHYtMkg1bTE0LTloLTRWM0g5djZINWw3IDcgNy03eiIgZmlsbD0iIzQyODVGNCIvPjwvc3ZnPg==);
    display: inline-block;
    margin-inline-end: 4px;
    vertical-align: -webkit-baseline-middle;
  }
  
  #download-link-clicked:before {
    width: 0px;
    opacity: 0;
  }
  
  .offline-content-list-title {
    color: rgb(95, 99, 104);
    font-size: .8em;
    line-height: 1;
    margin-bottom: .8em;
  }
  
  #offline-content-suggestions {
    margin-inline-start: -5%;
    width: 110%;
  }
  
  /* The selectors below adjust the "overflow" of the suggestion cards contents
   * based on the same screen size based strategy used for the main frame, which
   * is applied by the `interstitial-wrapper` class. */
  @media (max-width: 700px) {
    #offline-content-suggestions {
      margin-inline-start: -5%;
      width: 110%;
    }
  }
  
  @media (max-width: 420px) {
    #offline-content-suggestions {
      margin-inline-start: -2.5%;
      width: 105%;
    }
  }
  
  @media (max-width: 420px) and (orientation: portrait),
  (max-height: 560px) {
    #offline-content-suggestions {
      margin-inline-start: -12px;
      width: calc(100% + 24px);
    }
  }
  
  .suggestion-with-image .offline-content-suggestion-visual {
    flex-basis: 8.2em;
    flex-shrink: 0;
  }
  
  .suggestion-with-image .offline-content-suggestion-visual>img {
    height: 100%;
    width: 100%;
  }
  
  #offline-content-list:not(.is-rtl) .suggestion-with-image .offline-content-suggestion-visual>img {
    border-bottom-right-radius: 8px;
    border-top-right-radius: 8px;
  }
  
  #offline-content-list.is-rtl .suggestion-with-image .offline-content-suggestion-visual>img {
    border-bottom-left-radius: 8px;
    border-top-left-radius: 8px;
  }
  
  .suggestion-with-icon .offline-content-suggestion-visual {
    align-items: center;
    display: flex;
    justify-content: center;
    min-height: 4.2em;
    min-width: 4.2em;
  }
  
  .suggestion-with-icon .offline-content-suggestion-visual>div {
    align-items: center;
    background-color: rgb(241, 243, 244);
    border-radius: 50%;
    display: flex;
    height: 2.3em;
    justify-content: center;
    width: 2.3em;
  }
  
  .suggestion-with-icon .offline-content-suggestion-visual>div>img {
    height: 1.45em;
    width: 1.45em;
  }
  
  .offline-content-suggestion-texts {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    line-height: 1.3;
    padding: .9em;
    width: 100%;
  }
  
  /* TODO(sayyagari): Migrate from usage of deprecated CSS -webkit-box. */
  .offline-content-suggestion-title {
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    color: rgb(32, 33, 36);
    display: -webkit-box;
    font-size: 1.1em;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  div.offline-content-suggestion {
    align-items: stretch;
    border-color: rgb(218, 220, 224);
    border-radius: 8px;
    border-style: solid;
    border-width: 1px;
    display: flex;
    justify-content: space-between;
    margin-bottom: .8em;
  }
  
  .suggestion-with-image {
    flex-direction: row;
    height: 8.2em;
    max-height: 8.2em;
  }
  
  .suggestion-with-icon {
    flex-direction: row-reverse;
    height: 4.2em;
    max-height: 4.2em;
  }
  
  .suggestion-with-icon .offline-content-suggestion-title {
    -webkit-line-clamp: 1;
    word-break: break-all;
  }
  
  .suggestion-with-icon .offline-content-suggestion-texts {
    padding-inline-start: 0px;
  }
  
  .offline-content-suggestion-attribution-freshness {
    color: rgb(95, 99, 104);
    display: flex;
    font-size: .8em;
  }
  
  /* TODO(sayyagari): Migrate from usage of deprecated CSS -webkit-box. */
  .offline-content-suggestion-attribution {
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    display: -webkit-box;
    flex-shrink: 1;
    overflow-wrap: break-word;
    overflow: hidden;
    text-overflow: ellipsis;
    word-break: break-all;
  }
  
  .no-attribution .offline-content-suggestion-attribution {
    display: none;
  }
  
  .offline-content-suggestion-freshness:before {
    content: '-';
    display: inline-block;
    flex-shrink: 0;
    margin-inline-end: .1em;
    margin-inline-start: .1em;
  }
  
  .no-attribution .offline-content-suggestion-freshness:before {
    display: none;
  }
  
  .offline-content-suggestion-freshness {
    flex-shrink: 0;
  }
  
  .suggestion-with-image .offline-content-suggestion-pin-spacer {
    flex-shrink: 1;
    flex-grow: 100;
  }
  
  .suggestion-with-image .offline-content-suggestion-pin {
    content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCI+PGRlZnM+PHBhdGggaWQ9ImEiIGQ9Ik0wIDBoMjR2MjRIMFYweiIvPjwvZGVmcz48Y2xpcFBhdGggaWQ9ImIiPjx1c2UgeGxpbms6aHJlZj0iI2EiIG92ZXJmbG93PSJ2aXNpYmxlIi8+PC9jbGlwUGF0aD48cGF0aCBjbGlwLXBhdGg9InVybCgjYikiIGQ9Ik0xMiAyQzYuNSAyIDIgNi41IDIgMTJzNC41IDEwIDEwIDEwIDEwLTQuNSAxMC0xMFMxNy41IDIgMTIgMnptNSAxNkg3di0yaDEwdjJ6bS02LjctNEw3IDEwLjdsMS40LTEuNCAxLjkgMS45IDUuMy01LjNMMTcgNy4zIDEwLjMgMTR6IiBmaWxsPSIjOUFBMEE2Ii8+PC9zdmc+);
    flex-shrink: 0;
    height: 1.4em;
    margin-inline-start: .4em;
    width: 1.4em;
  }
  
  .offline-content-list-action {
    text-align: center;
  }
  
  #offline-content-summary {
    border-color: rgb(241, 243, 244);
    border-radius: 12px;
    border-style: solid;
    border-width: 1px;
    padding: 12px;
    text-align: center;
  }
  
  .offline-content-summary-image-truncate {
    width: 45px;
  }
  
  .offline-content-summary-images {
    direction: ltr;
    display: flex;
    margin-top: 10px;
    justify-content: center;
    padding-bottom: 12px;
  }
  
  .offline-content-summary-images img {
    background: rgb(241, 243, 244);
    border-radius: 50%;
    box-shadow:
      0px 1px 2px 0px rgb(155, 155, 155),
      0px 1px 3px 0px rgb(155, 155, 155);
    padding: 12px;
    width: 32px;
  }
  
  .offline-content-summary-description {
    border-top: 1px solid rgb(241, 243, 244);
    padding-top: 12px;
  }
  
  .offline-content-summary-action {
    padding-top: 12px;
  }
  
  /* Don't allow overflow when in a subframe. */
  html[subframe] body {
    overflow: hidden;
  }
  
  /* TODO(sayyagari): Migrate from usage of deprecated CSS -webkit-flex. */
  #sub-frame-error {
    -webkit-align-items: center;
    background-color: #DDD;
    display: -webkit-flex;
    -webkit-flex-flow: column;
    height: 100%;
    -webkit-justify-content: center;
    left: 0;
    position: absolute;
    text-align: center;
    top: 0;
    transition: background-color .2s ease-in-out;
    width: 100%;
  }
  
  #sub-frame-error:hover {
    background-color: #EEE;
  }
  
  #sub-frame-error .icon-generic {
    margin: 0 0 16px;
  }
  
  #sub-frame-error-details {
    margin: 0 10px;
    text-align: center;
    visibility: hidden;
  }
  
  /* Show details only when hovering. */
  #sub-frame-error:hover #sub-frame-error-details {
    visibility: visible;
  }
  
  /* If the iframe is too small, always hide the error code. */
  /* TODO(mmenke): See if overflow: no-display works better, once supported. */
  @media (max-width: 200px),
  (max-height: 95px) {
    #sub-frame-error-details {
      display: none;
    }
  }
  
  /* Adjust icon for small embedded frames in apps. */
  @media (max-height: 100px) {
    #sub-frame-error .icon-generic {
      height: auto;
      margin: 0;
      padding-top: 0;
      width: 25px;
    }
  }
  
  #control-buttons {
    display: block;
  }
  
  /* details-button is special; it's a <button> element that looks like a link. */
  #details-buttons {
    width: 100%;
  }
  
  #details-button {
    box-shadow: none;
    min-width: 0;
    background: none;
    border: none;
    color: var(--edge-primary-text-color);
    cursor: pointer;
    font-size: 14px;
    line-height: 20px;
    text-decoration: none;
    float: left;
    padding: 4px;
    font-family: system-ui, sans-serif;
  }
  
  #details-button:before {
    display: inline-block;
    content: "";
    background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzLjM2MTMgNC43MzYzM0wxMy44ODg3IDUuMjYzNjdMOCAxMS4xNTIzTDIuMTExMzMgNS4yNjM2N0wyLjYzODY3IDQuNzM2MzNMOCAxMC4wOTc3TDEzLjM2MTMgNC43MzYzM1oiIGZpbGw9IiMxMDEwMTAiLz4KPC9zdmc+Cg==");
    margin-right: 10px;
    width: 14px;
    height: 10px;
    background-repeat: no-repeat;
    background-position: center center;
    fill: var(--edge-primary-text-color);
  }
  
  #details-button.expanded:before {
    transform: rotate(180deg);
  }
  
  #details-button:focus {
    outline: solid 2px var(--edge-focus-color);
  }
  
  @media (forced-colors: active) {
  
    #details-button,
    #game-button {
      -ms-high-contrast-adjust: none;
      color: ButtonText;
      background-color: ButtonFace;
    }
  
    #game-button {
      /* extra border for this button only */
      border: 1px solid ButtonText;
    }
  
    #details-button::before,
    #game-button::before {
      fill: ButtonText;
    }
  
    #details-button:focus,
    #game-button:focus {
      outline: 2px solid ButtonText;
    }
  
    #details-button:hover,
    #game-button:hover {
      background-color: Highlight;
      color: HighlightText;
    }
  
    #details-button:hover::before,
    #game-button:hover::before {
      fill: HighlightText;
    }
  }
  
  .nav-wrapper {
    margin-top: 20px;
  }
  
  #control-buttons,
  #stale-load-button,
  #details-buttons {
    float: left !important;
  }
  
  .suggested-left .secondary-button {
    margin-inline-end: 0px;
  }
  
  #details-button.singular {
    float: none;
  }
  
  /* download-button shows both icon and text. */
  #download-button {
    padding-bottom: 4px;
    padding-top: 4px;
    position: relative;
  }
  
  #download-button:before {
    background: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAQAAABKfvVzAAAAO0lEQVQ4y2NgGArgPxIY1YChsOE/LtBAmpYG0mxpIOSDBpKUo2lpIDZxNJCkHKqlYZAla3RAHQ1DFgAARRroHyLNTwwAAAAASUVORK5CYII=) 1x,
        url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAQAAAD9CzEMAAAAZElEQVRYw+3Ruw3AMAwDUY3OzZUmRRD4E9iim9wNwAdbEURHyk4AAAAATiCVK8lLyPsKeT9K3lsownnunfkPxO78hKiYHxBV8x2icr5BVM+/CMf8g3DN34Rzns6ViwHUAUQ/6wIAd5Km7l6c8AAAAABJRU5ErkJggg==) 2x) no-repeat;
    content: '';
    display: inline-block;
    width: 24px;
    height: 24px;
    margin-inline-end: 4px;
    margin-inline-start: -4px;
    vertical-align: middle;
  }
  
  #download-button:disabled {
    background: rgb(180, 206, 249);
    color: rgb(255, 255, 255);
  }
  
  /* TODO(https://crbug.com/852872): UI for offline suggested content is incomplete. */
  .suggested-thumbnail {
    width: 25vw;
    height: 25vw;
  }
  
  #reload-button {
    background-color: var(--edge-blue-rest);
    color: white;
    /* always white because it is a blue button */
    border-radius: 4px;
    width: 87px;
    height: 40px;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 16px;
    line-height: 22px;
    outline: none;
    padding: 0;
  }
  
  #reload-button:focus {
    outline: var(--edge-focus-outline);
    box-shadow: var(--edge-primary-button-focus-shadow);
  }
  
  #reload-button:hover {
    background-color: var(--edge-blue-hover);
  }
  
  #reload-button:active {
    background-color: var(--edge-blue-pressed);
  }
  
  @media (forced-colors: active) {
  
    /* Acts like an accent button */
    #reload-button {
      -ms-high-contrast-adjust: none;
      background-color: Highlight;
      color: HighlightText;
    }
  
    #reload-button:hover {
      background-color: HighlightText;
      color: Highlight;
      border: 2px solid Highlight;
    }
  
    #reload-button:focus {
      outline: 2px solid ButtonText;
      box-shadow: none;
    }
  }
  
  #secondary-reload-button {
    background-color: var(--edge-light-grey-rest);
    color: var(--edge-primary-text-color);
    border-radius: 4px;
    width: 87px;
    height: 40px;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 16px;
    line-height: 22px;
    outline: none;
    padding: 0;
    margin-inline: 10px;
  }
  
  #secondary-reload-button:focus {
    outline: var(--edge-focus-outline);
    box-shadow: var(--edge-primary-button-focus-shadow);
  }
  
  #secondary-reload-button:hover {
    background-color: var(--edge-light-grey-hover);
  }
  
  #secondary-reload-button:active {
    background-color: var(--edge-light-grey-pressed);
  }
  
  @media (forced-colors: active) {
  
    /* Acts like an accent button */
    #secondary-reload-button {
      -ms-high-contrast-adjust: none;
      background-color: Highlight;
      color: HighlightText;
    }
  
    #secondary-reload-button:hover {
      background-color: HighlightText;
      color: Highlight;
      border: 2px solid Highlight;
    }
  
    #secondary-reload-button:focus {
      outline: 2px solid ButtonText;
      box-shadow: none;
    }
  }
  
  #diagnose-button {
    background-color: var(--edge-blue-rest);
    color: white;
    /* always white because it is a blue button */
    border-radius: 4px;
    width: auto;
    height: 40px;
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 16px;
    line-height: 22px;
    outline: none;
    padding-inline: 10px;
  }
  
  #diagnose-button:focus {
    outline: var(--edge-focus-outline);
    box-shadow: var(--edge-primary-button-focus-shadow);
  }
  
  #diagnose-button:hover {
    background-color: var(--edge-blue-hover);
  }
  
  #diagnose-button:active {
    background-color: var(--edge-blue-pressed);
  }
  
  @media (forced-colors: active) {
    /* Acts like an accent button */
    #diagnose-button {
      -ms-high-contrast-adjust: none;
      background-color: Highlight;
      color: HighlightText;
    }
  
    #diagnose-button:hover {
      background-color: HighlightText;
      color: Highlight;
      border: 2px solid Highlight;
    }
  
    #diagnose-button:focus {
      outline: 2px solid ButtonText;
      box-shadow: none;
    }
  }
  
  /* Offline page */
  .offline {
    transition: -webkit-filter 1.5s cubic-bezier(0.65, 0.05, 0.36, 1),
      background-color 1.5s cubic-bezier(0.65, 0.05, 0.36, 1);
    will-change: -webkit-filter, background-color;
  }
  
  #main-message>p {
    font-size: 16px;
    line-height: 22px;
    color: var(--edge-primary-text-color);
    font-family: "Segoe UI", system-ui, sans-serif;
    font-style: normal;
    font-weight: 600;
  }
  
  .offline #main-message>p {
    display: none;
  }
  
  .offline.inverted {
    -webkit-filter: invert(100%);
    background-color: var(--edge-black);
  }
  
  .offline .interstitial-wrapper {
    color: #2b2b2b;
    font-size: 1em;
    line-height: 1.55;
    margin: 0 auto;
    padding-top: 100px;
    width: 100%;
  }
  
  .interstitial-wrapper {
    max-width: 700px;
  }
  
  .offline .controller {
    background: rgba(247, 247, 247, .1);
    height: 100vh;
    left: 0;
    position: absolute;
    top: 0;
    width: 100vw;
    z-index: 9;
  }
  
  .game-split-line {
    margin-top: 0px;
    height: 1px;
    background: rgba(0, 0, 0, 0.18);
  }
  
  .game-button-msg {
    margin-top: 2px;
  }
  
  #offline-resources {
    display: none;
  }
  
  @media (max-width: 420px) {
    #download-button {
      padding-bottom: 12px;
      padding-top: 12px;
    }
  
    .snackbar {
      left: 0;
      bottom: 0;
      width: 100%;
      border-radius: 0;
    }
  }
  
  @media (max-height: 350px) {
    h1 {
      margin: 0 0 15px;
    }
  
    .icon-offline {
      margin: 0 0 10px;
    }
  
    .interstitial-wrapper {
      margin-top: 5%;
    }
  
    .nav-wrapper {
      margin-top: 30px;
    }
  }
  
  @media (min-width: 420px) and (max-width: 736px) and (min-height: 240px) and (max-height: 420px) and (orientation:landscape) {
    .interstitial-wrapper {
      margin-bottom: 100px;
    }
  }
  
  @media (max-width: 360px) and (max-height: 480px) {
    .offline .interstitial-wrapper {
      padding-top: 60px;
    }
  
  }
  
  @media (min-height: 240px) and (orientation: landscape) {
    .offline .interstitial-wrapper {
      margin-bottom: 90px;
    }
  
    .icon-offline {
      margin-bottom: 20px;
    }
  }
  
  @media (max-height: 320px) and (orientation: landscape) {
    .icon-offline {
      margin-bottom: 0;
    }
  
  }
  
  @media (max-width: 240px) {
    button {
      padding-left: 12px;
      padding-right: 12px;
    }
  
    .interstitial-wrapper {
      overflow: inherit;
      padding: 0 8px;
    }
  }
  
  @media (max-width: 120px) {
    button {
      width: auto;
    }
  }
  
  @media (max-height: 650px) and (orientation: landscape) {
    .footer {
      display: none;
    }
  }
  
  @media (max-width: 700px) and (orientation: portrait) {
    .footer {
      display: none;
    }
  }
  
  @media (min-width: 600px) {
    .interstitial-wrapper {
      margin-left: 200px;
    }
  }
  
  @media (prefers-color-scheme: dark) {
  
    .managed-icon {
      filter: invert(1);
    }
  
    .icon-play-game-button {
      content: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xNSA0LjVDMTUuMjA4NCA0LjUgMTUuMzk1IDQuNjI5MjggMTUuNDY4MiA0LjgyNDQzQzE1LjkwODIgNS45OTc4NiAxNi43NDM4IDYuNDk5ODkgMTcuNSA2LjQ5OTg5QzE3Ljc3NjEgNi40OTk4OSAxOCA2LjcyMzc1IDE4IDYuOTk5ODlDMTggNy4yNzYwNCAxNy43NzYxIDcuNDk5ODkgMTcuNSA3LjQ5OTg5QzE2LjUzODMgNy40OTk4OSAxNS42MjQxIDcuMDAyOTcgMTUgNi4wODczOUMxNC4zNzU5IDcuMDAyOTcgMTMuNDYxNyA3LjQ5OTkgMTIuNSA3LjQ5OTk1QzExLjUzODQgNy41IDEwLjYyNDEgNy4wMDMxNSAxMCA2LjA4NzY4QzkuMzc1OTEgNy4wMDMxNSA4LjQ2MTY0IDcuNSA3LjUgNy41QzYuNTM4NTQgNy41IDUuNjI0NDMgNy4wMDMzNCA1LjAwMDM1IDYuMDg4MTlDNC4zNzYzNiA3LjAwNDgzIDMuNDYyMDIgNy41MDI1NCAyLjUwMDAxIDcuNTAyNTVDMi4yMjM4NyA3LjUwMjU2IDIgNy4yNzg3IDIgNy4wMDI1NkMyIDYuNzI2NDIgMi4yMjM4NSA2LjUwMjU2IDIuNDk5OTkgNi41MDI1NUMzLjI1NTkgNi41MDI1NCA0LjA5MTYgNi4wMDAxMSA0LjUzMTc3IDQuODI1MDNDNC42MDQ4OSA0LjYyOTgzIDQuNzkxNDQgNC41MDA0NyA0Ljk5OTg5IDQuNTAwNDJDNS4yMDgzNCA0LjUwMDM4IDUuMzk0OTUgNC42Mjk2NiA1LjQ2ODE1IDQuODI0ODNDNS45MDgxOSA1Ljk5ODAxIDYuNzQzNzEgNi41IDcuNSA2LjVDOC4yNTYyOSA2LjUgOS4wOTE4MSA1Ljk5ODAxIDkuNTMxODUgNC44MjQ4M0M5LjYwNTA0IDQuNjI5NjkgOS43OTE1OSA0LjUwMDQyIDEwIDQuNTAwNDJDMTAuMjA4NCA0LjUwMDQyIDEwLjM5NSA0LjYyOTY5IDEwLjQ2ODIgNC44MjQ4M0MxMC45MDgyIDUuOTk4MDIgMTEuNzQzNyA2LjQ5OTk5IDEyLjUgNi40OTk5NUMxMy4yNTYyIDYuNDk5OTEgMTQuMDkxOCA1Ljk5Nzg1IDE0LjUzMTggNC44MjQ0M0MxNC42MDUgNC42MjkyOCAxNC43OTE2IDQuNSAxNSA0LjVaTTE1IDkuNUMxNS4yMDg0IDkuNSAxNS4zOTUgOS42MjkyOCAxNS40NjgyIDkuODI0NDNDMTUuOTA4MiAxMC45OTc5IDE2Ljc0MzggMTEuNDk5OSAxNy41IDExLjQ5OTlDMTcuNzc2MSAxMS40OTk5IDE4IDExLjcyMzggMTggMTEuOTk5OUMxOCAxMi4yNzYgMTcuNzc2MSAxMi40OTk5IDE3LjUgMTIuNDk5OUMxNi41MzgzIDEyLjQ5OTkgMTUuNjI0MSAxMi4wMDMgMTUgMTEuMDg3NEMxNC4zNzU5IDEyLjAwMyAxMy40NjE3IDEyLjQ5OTkgMTIuNSAxMi40OTk5QzExLjUzODQgMTIuNSAxMC42MjQxIDEyLjAwMzIgMTAgMTEuMDg3N0M5LjM3NTkxIDEyLjAwMzIgOC40NjE2NCAxMi41IDcuNSAxMi41QzYuNTM4NTQgMTIuNSA1LjYyNDQzIDEyLjAwMzMgNS4wMDAzNSAxMS4wODgyQzQuMzc2MzYgMTIuMDA0OCAzLjQ2MjAyIDEyLjUwMjUgMi41MDAwMSAxMi41MDI2QzIuMjIzODcgMTIuNTAyNiAyIDEyLjI3ODcgMiAxMi4wMDI2QzIgMTEuNzI2NCAyLjIyMzg1IDExLjUwMjYgMi40OTk5OSAxMS41MDI2QzMuMjU1OSAxMS41MDI1IDQuMDkxNiAxMS4wMDAxIDQuNTMxNzcgOS44MjUwM0M0LjYwNDg5IDkuNjI5ODMgNC43OTE0NCA5LjUwMDQ3IDQuOTk5ODkgOS41MDA0MkM1LjIwODM0IDkuNTAwMzggNS4zOTQ5NSA5LjYyOTY2IDUuNDY4MTUgOS44MjQ4M0M1LjkwODE5IDEwLjk5OCA2Ljc0MzcxIDExLjUgNy41IDExLjVDOC4yNTYyOSAxMS41IDkuMDkxODEgMTAuOTk4IDkuNTMxODUgOS44MjQ4M0M5LjYwNTA0IDkuNjI5NjkgOS43OTE1OSA5LjUwMDQyIDEwIDkuNTAwNDJDMTAuMjA4NCA5LjUwMDQyIDEwLjM5NSA5LjYyOTY5IDEwLjQ2ODIgOS44MjQ4M0MxMC45MDgyIDEwLjk5OCAxMS43NDM3IDExLjUgMTIuNSAxMS40OTk5QzEzLjI1NjIgMTEuNDk5OSAxNC4wOTE4IDEwLjk5NzkgMTQuNTMxOCA5LjgyNDQzQzE0LjYwNSA5LjYyOTI4IDE0Ljc5MTYgOS41IDE1IDkuNVpNMTUuNDY4MiAxNC44MjQ0QzE1LjM5NSAxNC42MjkzIDE1LjIwODQgMTQuNSAxNSAxNC41QzE0Ljc5MTYgMTQuNSAxNC42MDUgMTQuNjI5MyAxNC41MzE4IDE0LjgyNDRDMTQuMDkxOCAxNS45OTc5IDEzLjI1NjIgMTYuNDk5OSAxMi41IDE2LjQ5OTlDMTEuNzQzNyAxNi41IDEwLjkwODIgMTUuOTk4IDEwLjQ2ODIgMTQuODI0OEMxMC4zOTUgMTQuNjI5NyAxMC4yMDg0IDE0LjUwMDQgMTAgMTQuNTAwNEM5Ljc5MTU5IDE0LjUwMDQgOS42MDUwNCAxNC42Mjk3IDkuNTMxODUgMTQuODI0OEM5LjA5MTgxIDE1Ljk5OCA4LjI1NjI5IDE2LjUgNy41IDE2LjVDNi43NDM3MSAxNi41IDUuOTA4MTkgMTUuOTk4IDUuNDY4MTUgMTQuODI0OEM1LjM5NDk1IDE0LjYyOTcgNS4yMDgzNCAxNC41MDA0IDQuOTk5ODkgMTQuNTAwNEM0Ljc5MTQ0IDE0LjUwMDUgNC42MDQ4OSAxNC42Mjk4IDQuNTMxNzcgMTQuODI1QzQuMDkxNiAxNi4wMDAxIDMuMjU1OSAxNi41MDI1IDIuNDk5OTkgMTYuNTAyNkMyLjIyMzg1IDE2LjUwMjYgMiAxNi43MjY0IDIgMTcuMDAyNkMyIDE3LjI3ODcgMi4yMjM4NyAxNy41MDI2IDIuNTAwMDEgMTcuNTAyNkMzLjQ2MjAyIDE3LjUwMjUgNC4zNzYzNiAxNy4wMDQ4IDUuMDAwMzUgMTYuMDg4MkM1LjYyNDQzIDE3LjAwMzMgNi41Mzg1NCAxNy41IDcuNSAxNy41QzguNDYxNjQgMTcuNSA5LjM3NTkxIDE3LjAwMzIgMTAgMTYuMDg3N0MxMC42MjQxIDE3LjAwMzIgMTEuNTM4NCAxNy41IDEyLjUgMTcuNDk5OUMxMy40NjE3IDE3LjQ5OTkgMTQuMzc1OSAxNy4wMDMgMTUgMTYuMDg3NEMxNS42MjQxIDE3LjAwMyAxNi41MzgzIDE3LjQ5OTkgMTcuNSAxNy40OTk5QzE3Ljc3NjEgMTcuNDk5OSAxOCAxNy4yNzYgMTggMTYuOTk5OUMxOCAxNi43MjM4IDE3Ljc3NjEgMTYuNDk5OSAxNy41IDE2LjQ5OTlDMTYuNzQzOCAxNi40OTk5IDE1LjkwODIgMTUuOTk3OSAxNS40NjgyIDE0LjgyNDRaIiBmaWxsPSIjNEQ4REZBIi8+DQo8L3N2Zz4NCg==);
    }
  
    #game-button {
      color: rgba(77, 141, 250, 1);
  
    }
  
    .icon-elixir-page-error {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-thinking {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-blocked {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-disconnected {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-insecure {
      content: url(data:image/webp;base64,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);
    }
  }
  
  @media (forced-colors: active) and (prefers-color-scheme: dark) {
  
    .icon-elixir-page-error {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-thinking {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-blocked {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-disconnected {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-insecure {
      content: url(data:image/webp;base64,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);
    }
  }
  
  @media (forced-colors: active) and (prefers-color-scheme: light) {
  
    .icon-elixir-page-error {
      content: url(data:image/webp;base64,UklGRigMAABXRUJQVlA4TBsMAAAvAME/EIXnbNvkuLlt6+VvQYy6HiNGXbTAa7RGD+qOitAoWhUhCzLVGk1iOKCEBURaIMgCwgPBA4YHDA/yvS4CCER8+ALZVISE2tqDyNk6iISsg0hIFZQqmDgABxMFHRQMOMDBxEFxQBxsHHBpQZIUNpaaeYeENIzPgVH3IHn9ja/rX774jy/+44v/uGZgYLjqYOaTJwcR8eTKeKXBbzYi8hzHIyJu13gDaXhykNew4LUUDhzixWkdjMzMTNcMiF/tNaITA5alQbz5WL7hTCys3HiyO71Oo9Fc/39cLeA3xk/RRQ2C5T3izcyJM1ce7C9j1GnVKhbMC24sVwr4C1/jUANgzahzUCssB6NVqDU6nSPAdZ2Ab4wbJ/QI1nBjcHEEAIZVOWj1HI9m5cLCvTNUgZFBB/ALHd6hZ9Yq4A1yOiOHFmWHwMCZjYOIONj42BSM0+xyOf834Keci3sA69WIiGi/wPm1xXMGIyJi32KDgYmFMzce7E5vPrvcOHtti0Frx4Dwx5mNqFOCqZTOiHgwSA41Fq7ceL6MUS94QYHVttDL2S9g/tlwaBR6pyyH2BnFhtqg0whdUIxC7aAzqExtJRAEww60osGIegaEijEgdqbUoeb0WgehoWZVaq3OyKOpfAQ3BoFYq51GAjH/fzjhgBwDVkqLOLisDzVOs6E2moaaFR5qvfAFZeq7Qc8AQKy5sAPADoZDETNFg4jPpVJgYQ0MNWNtqEW9kffgp+jCioUThVL+QAGoUQciSsUjbhNhfh5pQy0Gj+CGE90Gb9A+AR1gQHFTpeWQdxAizKVaI3KoEUW0fQax9WifgAwAHgHEmmMtCDNJlYsS3KIXViwatE/ADmCQA5HF6JFHwuUEvsa5OIJI/BRF4g5uZI0QZU+/7AAWjQCEBotAG8y0V7RPLGoqsC1hNub/UWIX1kQ9E9p0Q54wr7AncMhIsIpoU2OmveLbsoMce5p8ewu36O5F287i277GScHvivKhxpTKnma+FRpAko2k8GLWZsSedELxOMKNonYlYJb2E2BPjen1eGkVGGdCJx3BT3kX0a//naTPq1rwSZ2KCHua+9fIsV6xcfePUrQX/JSTIRhnQ0qEPc39z5LtKPIkMe01TUlpwKITrA5Yg4hpM6EyRslWcMJt0toL3kkdsahKMYAKSZUHM2uRV0kzy0lvc1LasgTLAGoka9AgepBoo/S2J9FtA0rFj16KIW1HyQatNO31RpL2SkQP8FaKEVREtdNyfukZG0VswNckUc9UPFELB0okWUbWXHdvFdFJop43nFzBLA1y5rZVxETtJUHc8VGLAglbYTa/SESU1175wgOLpMuRUERjENMGZ3QSr70kpAvg0spAA9gi4olsRM+Cg1TtlUzd9gTUMRbzy0A04hFY3kUhnnqKwMCtFQYssGFEoeRMB2AkSj0jl6Qeos7MC1lLbBHRGJBTkOreseABOWLaKz4bi6Sz2gpL7wbRkZDdA4tISnulpKLwRy2cFWhTJEZv2ZaivcJZzBx1OHvpFZtaxUuO2Fi2DSS0V7IKw2tvsBAilkMjK9k6UCLH2jyR/xngUIo7MNgM5AhG7DiUTj1FKOjXL51gqy2xZcSeSMROqvYSIiD4UYveHLojjjZoy+jWDO4NOFtAd8TokXmLRFHDXeZdAp0E5pc0Pi6qvbJbkuHagsbGoIFMxETtlXlXrJ1IqEvOJFLP3Lvi8gnUaHsrJGfqhbSXTCYip3S0suSMjPaS0qEIGsEpMRm5faZecPlOTofml4xUkqlP1F7ijhmlolQlZxLvwdsDR0YyjAUyi9igCfKO3/rkl4lRkalP1F7yjjpVCHsBnDmURtxSe8Xeqa5Uh4/m0BTRoxPxNsFsXHYyVHGmfrtL3B9eulVYXhHf8rbBE8ChVIW1oqA/OfNTzn6cyKUDR7qw9G4RGVImnYtRLUK0de9QIzkJ0dvmRBSFYApycFVxH5CjkoQ9AryUcnBFWFt/0mjP4Jv/lVJQdeistOmKeGGYG0ErBVXmbKytP23VfU7Pq/CswUgZCvP1JzEbSVMwlQuT3I/gTBcaE/26J5mRPpOmYPhoJCBb56Mjb0HqQKBo6/6FymUplk+gpgoW1OTT0u+JHihpPMDogKWurQLS5ZYj+v9lq8auDEMRBgA9aoF8+SlH9MC+deVZ60+2C0aUXJtGUOhYgzNN1NOj6JNqDxJzU62cD7C+OuZAPS2HPtKRnDkBvHZIh8rcgwdn5NEzKzFivjeoMHlgZaC9DsgpjJLtlpPrwhwDGeCpQGtqO4pu88ia5pcXldSIQutSWPYqIe0YcBKtvQJTUoMuErv/mkGmnfI4gjPt2utBMFP/weYRX2jslLUDR8q1lxXK1N9y6ImVGDHLTllGUFKuvZxgpv6nnOTu3/Iy7JSRwNCtvR4sr5zWIgn7LDlTn2FSnqMAjmLtFRrVk/ei+6NUy2+XZw16KrSXwHNbk7dQxF52u9xbW5/opGmvM6IIeys5IjRy2+Uygopi7UVr5SNj8en6LDViZrvMHhiKtVeEiJCLmNUuA72eqFd7UcDkI2a1y34EZxtrLy9eewXftw0ijnLa5b4pB22BkaS9Am9cVPfvJUc0Wim7eKs70YHSttqrl0A9Y8vC+w2PHqUmZ/LRIcxkGN521LOSQj2TtKQh1P17CUtzWNSdeAcGGrVXOKMUHXGUbO9ko8XZW9BSqb2SbO4tkZx5L/4J5n8mbScOoKRQewnklGT4+I1B9IhH1XYiGcZ2baV07UVEm0Z8K5qCaDuZiUqbHBgADGS0F6VGvJWYqf8aL5aCqLtZk6MFjW20VxL1lCmfSfDxG6NMTmYbQWmb9LuM9hKLKP1Ey0VBGwtlJQM8tdpr64g3zjJhocxUgzNF2mslryMZUfix9hfabtRi4OhATan2kov4jkcfRMIjyqNjNg8MVetPwuVRWqb+DSLKo2PWqVPpe/A2o55ElJSckXyq7+KesoqZhBOSFoBDm1FPSkzOSD7W+kxbxSG72wEo0WAT7UVEJJuc+SknLSeprOIx7YrWLbqnoS0yUy+4Uv9EWcWFGoIkdAQAAypF4oRoW3vLC+WpjUbyS63oqhjIEdxtTYg9UiLJEp+pp0GjUqocdCT+PIKyio0sud2jOVKp53bdQy3itefSCSs15JxrM5V1J1Z7bWuL6ax00Op0WiORF2qoqphpAIYkjqghpL3EhU1p6SHl3gD8U9UpGVK7M98CjUTbRKldp1GrNXqe3F3bqp7f4kpHUBHCJzA7UFnHgDIsDfjWR9kueDLwjNl1xjHWqacuCFbIqnYtsdnj3nyiHa3YPcqzfAD4KHOGgZQGi/mK9wPSj/iU1O8nTRzMM8Qm0BOYG3UWG6UBZVueAC5FEdheq1cTbJpx9lGn0ep5pL7kosWYyTMSzVljoQDWmUP5l89UEXGuNIhfD3daNWuiHQuOGeqnUKrVKiPKujqC778VHWanznxArZKimhHDMp1OYeFxFqx2PwIjO/Ws2UbtbOA4zvQ3nkpGgs7wBr3eaMUj4wiaTOBpO4tSSsYR8NBk3IkeGIk22CF7Al/70ZWT4iDn3jZ3kucfQVnjKMmptEOgZ+ruVuLETtRJ2DBoj6o7+r7biGW2sY8HvFHnoGKBxu/4Y03ZaCmBlqTN4p2x/nWp/Ia7aeNB3EZpX3zBqhwMvOkHQ6jc4E6xFyJvR3w7c/7Hwfr6FyCz2mjsiS9x8OTGmZlB9R/BZCPqWZmTUG+U4ssp8veS5HAhOsvqyhLwrYn7quKk7OtOlpeVr1GoNToOCfnqjnEnbEf5+LZ6S1+2sG+OGzwnJ+0kzAlqfqMU8mXnwVVies0lxoMgD3e0+dYKRmh2HXgBXxamHfl5QAysFI5R8HT6jjT6KpanNQVTTG1ldg1dWFi0/RYgxfK0oWZ2Fb6w7EMMZxmjtvXnLDy76vTNgpUXHEkOKTLF7OxGabEgkz7YBmtEKsAh2bmxSvjuYwxrED3YnM70Oct2islHmEQuyy1+9Urk5yzoeyU2BqXl29voDAaDzqy/0Ocseoq5MhvOvYi1C6uU8Dm7UhvUuxecXHf0c6ZoJZ87BxGNep3OKDDY5teVa1o4cWfPeLDtiD5jZmZ+/YFY17988R9f/McX/3FNgC8A);
      filter: invert(1);
    }
  
    .icon-elixir-thinking {
      content: url(data:image/webp;base64,UklGRkQJAABXRUJQVlA4TDgJAAAvAME/EAWFbNvzttUTBhoDjYHLQENwPARxESRFECNYg2AOgpODYGJQM4gZ1Ayq60psSbbkT+e/ERJqaw8ih3WQOkgdUAepguIAHAyrgChYUDCMAxxMHBQHxMHEARcWbFtVm3MgICB5t8g9XPJNV35++o9P//HpP/6eBYFIJJb6BSfxYOeg0jAllcJBZqAvah0bJwCtdtDqTNhq1QwFoHIwEosIEjsNSuOs5wQ5uDqoAJTiFRBYaNBOLCeag44BsBPLllMOZiULCk40UEgFy52MnDXY0QrVgGGeWyvDD6E0IFJgDJwV+eEEXIU5iURTrpyVeVPhZikJWDylaxcWo0sCO06cJHyjcdEXInIqHScRbzQ+DEXon6r0nGR8V+NmLEHUBk5CftjjZixA7T0mDiThwfGoTRwMPvTC32vHSc53muh3yoATJwPeKLwl78FwsuAv3Mxig9e89+RtjsTugAkXjpNJqHBJXdZwsuEvIIsMVkzKciniQ5A49feYwV0pPIU+Jye2uIkyp5klMqd5JfJWP3rJLZG2EybM0qw6kTY1nOz4i7DDUBZY+eGDqNdiBNZ7LxnyBwHn5wlE0oMMLLRJzDA5ATsDaUJ6gQYjd5kFJw0zKg3LyZQdDR5SKWw8SGJ84Jg4aECl0epYvcGDTs4cDR60rKuzg1oFAIVMkkFnYZxYI2eLHFlnNQVUdtK2cxQoJwNn07T2NHAxEjacMyxHAF7VQGUhbvJvDscjJwRv9u6ZTQotXjl3CpLhIm1tjDW1tIuS0cDPpmYZOLGBUtmEDESq1nMk4s12hAz0E0uzTKGyESM2Mf+Y2oxfgiieGZ+Qf8zAjE/MX2mQe8zCjE/IfY7pwpGObxR+sjczyMcf8m5D1RwB8cHgf9ZleTbKceKaMW9Lu4wJV952NiETUs7nSJnwFiYdnTVqtZYVOZ140KgdRCr4rVbDOLgYpAqvuAmZpo1EuZaCCWPetrP5I7qIyBmYspVqFMbNJIihdaDBw4sQjuDhUfCTAw+/GiSSc/HMEpw1Jwm8EQi0agHR4Xfw8skojQ07y5PpEw2+W/BDG/nQQ4BWYFZtwqSVP2VZQVbSNFIQ4JkPRgjfeF81BPBFkuQNN/+kOP4DQjB8bwlC2Bn5/nkGH9GFEA0JiY6PgvB9eq0weh4gyBdpVAzkHBXnvSRoIEifiRnxn693YTxLAo01P7ApTpqbBfhDGFZmN1qGXVGMNDgLouIbl4Qx8L1o4WIhQGslGn6G4B/DVkJ44h08hN8SGQ4IuHLS0AjB+xp2Fny8bsI1aZBfE3pYiTBQ/DhZ8J48CUymAenH4BmubiGlm4PqecPegqsTbRCyKniHXz0prsKY4DyY9ioswow/2JujNgobWD0D00Eq41yGYEZSVVlNg2JM3DZEZCpQtAMrzoWHoUCrPZQfUtyQ4WyYQhSTtS1DiIkINnFxxCfnAWihJ6SJuJij0BPSBOr9WN6EJS8tltKTFx9Ocgos0O5R4gAuxmx8Lx2MHJl5UwFPQh5SJMuRmz8oXMT0kSaGITahByD6HKRosvNdhQ8xFynaosZFE2uxYhZHR7gSO7wBOQchwkBTXsld9GGPT1IhwjyGBiDlvBwh4mIWhe/sg7qZkwsR9iI6LOacBEdlZjq5cIRHI90FKaU2NatpjvjgSmeIn9qPGka5QZmhUgCkLj7DSHr8hndqS/wIZ9LD4EhnhpvZIQ1FlGRbKhUCrTUzrFZkD29STkyzzfrtKQIMwUaDnjVY++1vPclAr0tCy2NYrZ1Z2+XVgaEAAKAYLWs1nhlo5SBSYfOszOpUsGUqtYOOdWfnwFCwHg1rrtUkpZ2Iqfg+/L1ttjcQ3AvC2gOMK2s5ByOPRoV3aj1Gw9k0XynKyShqif5XV6v6ASUmF2TUNtzjuwa+G0VOsRorCpdbIGfgoEHrbdecoLxaYmz5brTOW3cEchYGCTSsjc6kf9VbJENXnqwRftFy0WcwUaEdXPUGG+NNZaks7Y3SGCxjr3OggDd9PgJlXlRsgJGq7UVZLCaNjZTbxlwkpk2RY+fVCv9XwLbkcTOQpN8XhN/UZxn4eZYdfPHaGaT38yx9itZaphZCsUDeGazm775Yx9Rn6y3NLRX4u2OtuDS3VMdfrLk0t1DHlG/WXJNVKNBerGhq4H+hsHO25trkQo0+dq7WdFBQKliTj9UqyzR+Khx2LgqOi6klaY1xeEskEHhwUAHa8q2bSWycNIDGyc5IiG7yofJM5iYsNBgHnbOWAbAsfHRKo9XptGoVUNmJ4RH4i+mr+oXEY3CCT9E92AM1upCeOvEE7Ht8jMGL8CfTa6wdawV7K6s4kap4X6ueRiXEgQcqVmjdYvBDyvfOaPqyPsvYQUW+Lq5CTg4HCiVu2UOM7P8EPKMaOq2dwQoXYdLtanYFhrX2/utws0RdhLzTvllhcb4woETo2IyIhEitOVE84SYFDnuzybZW9vud5L+kzQJ9jB+wNTzP8Yv2bG55aok6G8sUo+IagTli3d86zgfJO9Ya4Sd5tsJlux+HMxp7WPe90lCCL84no3mIt0zdiFAf86JWWsEK9vV2vvopYD/nD174/FkZF6Ood6rGRRQHbA80QqiEQI+r1abV+PZNRnQqQKXWCD7ilkR7QTPfi4+UEBRy2AvSatNqfLF5L0IHZzWj8ipCcCDQJj+wHAtnodNIUf4fok/mGRyIB3sMR7F2NttTel7sUaP8P4xgrSQkJeNoFP01NaSyxjHDckYVNDyZAYJ/H5inuFhyEzgB2kWsKkOu3wPA+RhdnSjA0UzWSI1c/KIcRQ6nWKOM0zCsKDefvInCbfI/umr1JrFCC79AxMlpDSXyNMZoVcxZz+/jVZn+PhLBgu/L0lGoMcoY2qO9hbMYXHHTx6piOADFaLTubFQU0CY7WokWeEE7uHrIahVQiPHS/5oyiFlNwLVEFEPm4KQCVE52HiQJjZCkiY4p/hNCmvQw0rRwuOFmLMrPPSEtUQZRtNFU9X0U9NrFRVdKEu/Vj+wJUKn57uPVPS0mmTFb/tGpGSc+376sdAUlOWZofaHcrctlDbXAGaMjcBDoykomKhoDr9N3GjNdcUlko6Fy0LGuJmtPKMQy/x4wJo7pMIXCg0BXcBKJBLry89N/fPqPT//xNy3oAA==);
    }
  
    .icon-elixir-blocked {
      content: url(data:image/webp;base64,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);
      filter: invert(1);
    }
  
    .icon-elixir-disconnected {
      content: url(data:image/webp;base64,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);
    }
  
    .icon-elixir-insecure {
      content: url(data:image/webp;base64,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);
    }
  }
  </style>
		<style>.neterror-vnext #main-frame-error {
    margin: 64px auto 0;
  }
  
  .neterror-vnext .icon-disconnected {
    content: url(data:image/webp;base64,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);
  }
  
  .neterror-vnext .icon-thinking {
    content: url(data:image/webp;base64,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);
  }
  
  .neterror-vnext .icon {
    height: 128px;
    margin: 0 0 20px;
    width: 128px;
  }
  
  .neterror-vnext .main-content {
    display: flex;
    flex-direction: column;
  }
  
  .bing-search {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 80px;
  }
  
  .bing-search .search-input {
    height: 46px;
    border-radius: 99px;
    border: 1px solid rgba(255, 255, 255, 0.20);
    box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.12), 0px 4px 8px 0px rgba(0, 0, 0, 0.14);
    backdrop-filter: blur(30px);
    box-sizing: border-box;
    display: flex;
  }
  
  .bing-search .search-input input {
    border: none;
    padding: 0 12px;
    line-height: 22px;
    font-size: 16px;
    background: #FFF;
    border-radius: 99px 0 0 99px;
    flex: 1;
  }
  
  .bing-search .search-input input:focus-visible {
    outline: none;
  }
  
  .bing-search .search-input input::placeholder {
    color: #616161;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
  }
  
  .search-icon {
    width: 70px;
    border-radius: 0 99px 99px 0;
    background: #0078D4;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  
  .top-sites {
    width: calc(100% - 60px);
    margin-top: 70px;
    display: grid;
    justify-content: center;
    grid-template-columns: repeat(auto-fit, 110px);
    grid-row-gap: 16px;
  }
  
  .site-item {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 9px;
    cursor: pointer;
  }
  
  .site-item .site-image {
    display: flex;
    width: 44px;
    height: 44px;
    padding: 6px;
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    border: 1px solid#E0E0E0;
    background-color: #fff;
    box-sizing: border-box;
  }
  
  .site-item .site-image img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  
  .site-item .title {
    color: #242424;
    font-size: 12px;
    font-weight: 400;
    line-height: 16px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 85%;
  }
  
  @media (max-width: 644px) {
    .bing-search .search-input {
      width: 343px;
    }
  }
  
  @media (min-width: 644px) and (max-width: 956px) {
    .bing-search .search-input {
      width: 400px;
    }
  }
  
  @media (min-width: 956px) and (max-width: 1268px) {
    .bing-search .search-input {
      width: 528px;
    }
  }
  
  @media (min-width: 1268px) {
    .bing-search .search-input {
      width: 780px;
    }
  }
  
  @media (prefers-color-scheme: dark) {
    .site-item .title {
      color: #fff;
    }
  
    .neterror-vnext .icon-disconnected {
      content: url(data:image/webp;base64,UklGRqYZAABXRUJQVlA4WAoAAAAQAAAAAAEA/wAAQUxQSN8IAAAB8Ibt/2G3/v89Z9YKmiqq3a14o7Zt27bt7dq2sd+omdS27dW0sb2S1/NGZyYrmdfr+bq5I2IC4F//y6jz9JaNC8ib6gcFT2J85odCJWUNBtXrgYiYdWMGjCkkZzCjxVeYPltZOlfSvp2T9BXerLFovqTBmOcaycc2/SFrhbTw1sWVsqZs1Ap9c0DWwC1KAzFsVj9nOYN2dq3UeuUmK3Km7tTCjco8FzkD/wSt28oKi6QpJ7W+qNtA1kdosRabpa1QpgbuWyFtykWttIPSBj218IUibZ4ftJ7KG8zVugzS3vmt1mlpU7aj9vVSsgaDdTAsv6z11sOtVkmrYNdLayBpRRL1cJ2kFU82cESVsyJJBg4qcubPDByTtCZocAfIeUMjexU5G2JkC8j5ZCMrpMGat3Bp/wpVqgSVK+7unHPKGgNsjAwUqDFg/vGXEQkZDBGZPT3h081d41oEOOXIMyNtiGct3W7pHTs6OO7A6Or5HeWabCAhkHQlRh5MwpxlD5Y2zuOQymjwoQvdlCZHozE3sufTSzigj5H5QPUiwz9h7s04UiVbMwywtkQr+Gs05vKz9a2G1JMG7MVJ5jYuGk143MdIhUQDDxWCqU2foTlTNnvpqDvQ4B9A78In7Gja9x2tGv4RBlgdcrn0ikczs8NeAFDgIRp84UStgjsYmvxFQ4D+aJBNAWJXfoDmT59S5pORzO9ppfTJQC5GoNH9CqmclqYhd1N/AkoXP4AcDgFKl7mLHM5oRqkKb5HHZ1RC+XxAHtvrAZ2rRiOXd6l0ahaPXH5eEsj8Syzy+aEbmcq+Q05n1KaS0xHkdqgrkXogx/epJLK+5Fl6MxK1Qq6/dqNQMN/YDAJ5xfIN08rQpx3yfpeFPMu5lxZAHeUY93Avddwe8i+rOHEKhfEPVxCnRJIA3nnRpmyaANhI2pQRAQZbSVMiSQTp/qQpFCkCNoI0+Z6KAE+RRg0WQro7ZWCjEFgz0kwQw2zS1GIiwAsKZQrFCSGyIGWUh0LI9KUMrBcC60maJkLA30jjnCaEnaSBg0IIpk07IdylTeE4EdhoA7tEEEWchqkCiFNoo14TQLKVNjBMAKnUcQvnX6xCHJjJv3Cgro+dex+pU+oBcv8ucco/Rv4H0ybwLQpwr7C828zefuru00fXTm6f1z3AzUHV41GE88VUcto9zGb8ud9rWrPXIgZFyHqJqPjsj+hI+53fgxRjvSNQiHY/AfWzocMzb47zMDAgC8UYk184TvsZ5mjiklJaM7NQkOdBtAVOY47HbPwWwG0OipJNE823dzE3Zqz1XYziaCqYMi8xl8baxZFRVCwV3iE9Q0CoP4YhPdkoofh8RnNf5VO8nzHFYlF4FvARzX0szzIuhSjGABTV4qzwyvsZmnu9O7jf4hAbCY60WJ1UHqlr0dxrFQAo9oQ/oSUdwutFaGo2GzQrJXBnMYizPzNV+gyrFnTL4Iz9O3FUTkVTzwJ9ZTLjyyEQZsm7aO642noAq7mSFSAMZS+aPXGIgTx7eLJTEUZfNH/GcD0o8F9+pPuCKPPbOIAJY/TA4wQ3FoIwdyIX2Vg98DjLibeuwqjE+IBsqB64hnCBdQVRqiHIy6yJeuC+jwcbFGE0ZNzAtM56kH+T+b54gjCPI0fD6umB9aPZUhuCMOsznmCMr477XjQ5mwjiPIl8feuiUfQqmn23izgCMziDwQUAoNw9NPsdLxDnQuTuAoDAF2j2F9+AOK3v+JPaoVoYmj3+BxBoY+RweBqa/XMtEOn/eWT++JYgUvdYgsQ1BqG2RHrGNAKxLhFFxrx7LLckVAfB3hVEWHtQ+z7LHS8DQbDudjG8qQoA4DX6aS647gOirYNCfFcetIvM/JRT1wqDcIcJ4X5RMJi3xx17DmSstoB4V4kg2BOMK1U32xz1qoUKAj4rgH35IPtqy11RDng3xAWE/I57bJ0rONa10pC9rxOZFot/vLi+CmK2JPGOTbdCDqpe31dt2bFTmzq+hVQQdlnGuZQ+QN6ayPmbFvq05V1aTfr05B3up88w7sWWJc9I7uES8gzgX6wLdbrxj3WiTmv+4UHq/CKANBfieDL+sW7EURL4h+uJA48F8L4Qcf4vANaIOH+JYAZx+ggAjxInUAQvnWhjjRdAYgnawFEBsCrEmS6CTsQJEMFY4kAY//AP6swVwGLqfJ/Mv5XUUa7wbwV1YCD/FpGnaCTv2CzywGruDaJPsWje1aMPzOdcemkCuafy7bmVQDCHb1uAwu5hPGMdSQRN0zj2yI1Gyn5+sdFA5DI2br33phJ0Y5xiA4HMTgs4ddVKJ7AGc+mZNxDadT2PPvkCpaczDr2tAJQenID8fVoOKP19LPL3eXmgtMtN5O/RvEBpZQHy94AbkLq+3QjjQ/J0VyC15TYajOr8gAdRLYHYXdDg87JQbKv5Dn4PxLa+MhAVBADQO8FcKf2A3JNRP7U9aJYMMdP10kDuYmEGVqpa4DI+zCyfpuUHek9C/cwgMOi5wRRsaykguPWJgduqEYDqxzJzGwuuCiRviga7Q3ar7EzPTVnbqwHRtxp46pwtgFIbwnJL6LpCQHWnUANNwaGe3Q4m5VzU/q5eQPc6TM/m7hgAcO+w9nGG41IfLmnuBaSfhPo7ISfdqozefj0+ewk31o/+0Qmof8zAwBzRdC5dvcvIeUtXbVy3Yunc4Z2rF1JBCp/pxRbIOUm1JOqdBUkvmqo3WdYGo343WftDz15H1nbpffGQNMWm9zK/pKnReidA0p0+a7GH9WUNWkZp3FNB2pU4jbB88gZaWb7y5sU0sI+8/Yzaa+WtVyrTeOEmbZuPZmlk1ZU15fJ81N4ga1UPj9eJC5K0FcsmYmYqMsSsLXLm9OdvK/FLKH6dXkrK6lefcwFttq9Yykopm15iog0/fPgq60m6v4R5jm85CvHDR0SGaafTbT7y1aTSuKmINhuy+xmR4Yfwf/I1Q/1tKsMvH/Dp+3fpqf+/+kd+6aoBLQY93xd6mx2as/HW/C4WkHLFQylRd/gqJX8B+Nf/EgsAVlA4IKAQAADwTwCdASoBAQABPlEmkEYjoj+jI9UKQ/AKCWVu4XJ+AMgMcAIj08+si4n7rzwrX/meEgND3O+bOqv5gH669QLzI/tN+0nu9f7D9d/eN/Z/UA/l3+n6yf0AP2k9Or2PP7d/2eoA//+ua/Qxwo9gDQba14D8FtFtdhSWv954Isy7+n+knnXesPYG/mH9m6y37ieyB+t5EfABEXjjqQAIi8cdSAAelSUHQhOkLL8fC3GNwbjqQAIi8IG27MJBoRvZDCjM2vABEXjcBMpkhGsmLuGwCLfQQ11ocwgYneemHycJJKvrCbFb6xSF+XyXgAiLww4j2jh3zWRA5phZl7GRa9J1VoVFht02VIpBj8D87WvKqs85BT9/KZIbxxRrjzoseTVhgaN/QHnhuOzhqRdRQCa8RxzgtpUk28qiv8pr6zQZEffj6SI9q+CirbfbcwZS3XRaaWwR/vzoKzIi8NsawD6TpEvOqkx5qk7K0mYvSFpTkKyaXwmpHlg66r4M4O943uDbgJtuU0TMhHUNR4YkPsmTYgjHKxo//Xq4Hngb8rfq6mtj5U6o4aiMbD3ABCHtfGvjykd8Q7Ie18CSQkDRHSoBYiu5h3/k7uHD29xOC/xykyKWwarWKJM1OmMOlVV1K2Wq0K+7gxjHjJz0T1iN0HItTg+RhKS1l6Fb5zArPfp6nGFcOxx1H3vUuXWq6f+tvxNZq8O8HtQhyAYdok4S34vm6iVmajUyOGrujjgtpVVm08BPqdwiWxKXmuw8ou8JnBr/fKISanI8+5sdmAV9JpqufpEReOOi4Kair4w4a9b253c/fMc7B4rjqQAIRESrS2wnPBb6BP87NnOg3HUgAJ0t5VsakACItwAA/vstAABgzOj9ghY2wMIBrH25KEeYD/Rw1yUjreNJLeHOuTOLTcoQpid/EX379HjQqC/zblFywLk4PejLG4Lu5jhNlmkbOakrAx3gXr0n/AXCquWYQw6Uk91Vbvb/t7NK0u60JaBD3hPrxm36bCd3R54NedLlPsqvo0vK9LqUw356Kvn1PJ3Ucu5qXCxLUJ3s1hXhxAALa45zhKvsmlEF7a36exgv6A6PUcjYs7kjlhyhJm4sh7RnfCtpLE+jrpoEoHXzyVFZ57TnhvbHOfOFw6f07fozPr64b3FJ1rq2cN42agZD8kMnox+S2XjSRx/3PjRaXd0W2n/tSr0YkXrEX9+0sgBiWxjeLGlojPPzUg3e6CdVT65IeAzf81CI/5Qu6YWRUzIVMdvtMGyw4/8tNVt2WRmGKqGbWmZ5Hl7q/DTlR55g0zwwK2/R8r9CaQxJrniMBTyjcFsNXnxeNlxAFvmLtsQ01twesOdHS50elxKHiUt0GiiumV5BHTGI3rfFq8FQB3kEmI6SskDLSAxtvhHiPfvtPgMAbxGhDGw0Y597kot79MDrHL2eKh5bMQwQ89Nz9j1clIzlXE68HhafwbMWNfOq+JKVblmzbrgMz8Y06Mn//t97E91cS77xSV31xI18q84g26i9MnfeO1n9Kxv4SgZMOXqJGXTjEd5g0M0Vep4MwcVaPgjN3aroRYNMbZAuTvCxp+qRLXS7PxnyS0H3Rbn/gb33fyogdEbX67jCZC6Os7ulBp2JzZ7mDlbz0+JNXBDKZVn8CZU9zpXYpyfWqAL1qv/r50iQU0eTKamiKagEJ/w7R4BlUrSicO05eWcwSu6iXeNUcp1oPH/zjHC2ne9uA55SIZoshGWdnf6GwlRpgYPJc3txEwbJtOL4YrSTNZSD4l0PGSfX3yCq7DYq2gRVrJ3CL7rgcfCx6lrh8hYXYc5yd1u3/PvLUfTGH34K/axKEXxw+SnMKaEC9QFP5JFlUeMQqe4ltUDGK2DivznFp/I1qo/jVKtzZWvrGKbDre93XhzXfdg9cpRcVtdqTjIsx/jYy8GO79BRqh22zj/jtMCD1egvmlYnFOG7aJb5DuMdbhYfkDZxD4u40D+cxTqCgBKB5194ONp7tdsjy2VRJ+tt6aszS874C+vAvlPMxi3dRcIpomNP+hJjRhvRYnuFlvQOHU0pF14S++fSkY+PWcXCQXp+kqHl9zszWhSX/M2cTg3egPKjFD/AdUmOMwuxksRfyiDWutetlihFXM8zaLz7I9LW8xaI0yc/njnj6cwNPJ8sbzqrMPAUn+UjD7S4hmkQ2IzlsNb/T9KYzHURoqwFx78DKi9lABQujDf8EFAtD3pf//qc/k1//djhBty4GjOdjixlduPBxnlxBLaDu45tg5GPB8wrX4F2BAZgueZW9kyCIzEFRnOcGa/1dBlv8keEjyNFDpH8ZOPR6uiGqD0zQOiUuwbeCDBObzm3PBQYc6MR068OHtrC97/I6x5FlEsEKutYPkmbp4ZBKJRTchBhenMQ49o/5aMn/ykyQ7obS8mrJlZn+hG67+34sBAOqo/ucuU7vypXtAERvPlYkMW2XfYFcPtzgGqMUpPnzUCs0lDuUuyJ+SP8StGMo/Oq7AVAphIKZOji9pWOsSBa/qCTE8UMs18vGXtxq9sVAO26cjIOJuru9fghcSZgfCJQF3DUoCPF2itmrqHnWRwhjwQpihfCPg/lPkiYcx4GlO9SuT4l2hMuhhn//SnxkSH8tgxQxqmPIeU8xHGFRTUVhnRYhhJGgPPfaZ+bMMR8zsWd74Zpg8QhN2ZrqXtEQ21ZpYr9zDlvOoihSl8CMoUcPMjbCDAR4xBr7QEa7sf6cPxIXrj5wufiX2ixJvH971+K0cJ4egHLkHpK+8xSAHXPa5pIw0H3uCJ/8ig+JUgsMWUdj8ldnl944ZkbR9Fozyu3fPfKxx88bN0gAI961HZ4Fxt5ECsjXLWdPSXZ0ApPFUnoZl3PsySVLtXazq4VuJUSC4A7EYp2zWXK32Ni8ILaBEqZbyVCkOF9Zrbt9GCYQzNvrb0LbfALB5iSljHnkN2lE0jfvvXCHriyTNtq9t2eSrn+x/utz/7dm4zjDEB2mxX1oCZyVYXRYpVcWuhTeOmEmh8onX8AiHcWe1wrWt+9ouoK9XYUK7IklCt5J11yswTAAPcNf450Cp8cMlR5SwdATL3tfO15kuQlsVV/rRa42rdtb/ukIUt+DX5azRb2F+p7sfetxiYLxtpdWShKXHFXGfxVNUUdAfBcqfDS+YYjMo7eR4rj6W0dgO1THM66mL+4axwyro6sxd5QeO7ZNeO1USeN+bcm49JGFbEWh7qogTmDQfEwEcxWMlBQxPDzFgLvyO/CuDiePl71GKNXXC3AJ0c9rkQzTVa/5bIe1EcMPfZs5mUyvg3lApXp+pc6guYuRS3UaNB7268p3/ns9lCtECreSj3g2Kb+E33nxc3pcmprtbDMbhr3nIYK/cr2PrZEVVE89ad+pfGzPN4jBNrTgBpO1lf733pqH7eVClSj0wn+mcMn47vj5hdRZVZ7qrkJjfeFxghv8V59FaXYtRlTF/bwJIkmOCPSy3ria26jWkNqOdPgeOtxmlYxsTLjDmjkYwd1oUKlrJyjKU1KywRSnVQ9pZcHtWt3lH/PE3Hy8xnCFzug4uwejr139bE7Kn69VcbBu1IgKBE8pCvFeWxQ72mlAlGDCcSkCSHrLAjbf0dO/RnWjtr6+D4qWLZ1mTT/KIzn3ff9hikbObUs9G4hZqge/n+yp2kiGt4CZ3P0kDqkAzRZ2fi1ZvqX+N/DvZSS7zn9KePfczdxb6YV059fLw1zJ/xlHak7Lv8LD+dhQ6II3I5FuUWIxVeGjyI7gplh+2//VXbLleX01RYQPqxf9+ONc1mLmkh6Hkdbhr8UUeTfbQXB1djyh1iHHD8betYWcSynvqgWsOBh4kQ1msex648gOvHwyvddDpKCJmx58laHBEe3fdXqJGA3DkWmt9QnNuLkz+/8Tkp/85kHotD+aXgkQ3t/gDoKUx4J6Iecc28iGuU2ECt1G9o9Z1Pej9BZXhgozWQKYLc4Y2HqODwvHa7KoBFMADKJU1Jkl2M0qreoObJE/ftIcQt2GyLuevwMtgLumLpCpElt9QUXyj9LcSbdml9XuSSxBXEjWYEqPQWabFG7p/fbRdJaiAQeA48+S8qP3ePPO+UtVrdw8fbWUiMmra9D1A3jx3AZF1HXvysw8qLkRZRxORlzAFApdZGjZvGPVs6WgtYo6uEJLwg+rfbDE79rPKPO0e/LYGs8pWF0ShGp08xWpVbIwh4hzPg2XLJq/F54qXtCCzj0ddkF+ELt4z0mKvPWzycxA4oYbCHBM8zPGRg4p0cHx5r6D4uWDAMJLdPgn4dWYUZES5fPszfxOaqIZJcCCRh7XlqG87ZKOTa/IFYYtQH5yAisRuyqktv6n6xJiW/PAuKPYO5QL/hSGH6gANvIufh3cJqgsSDvIxlOJZMRAJbXUaQd4eLBBr//T/bVpKK0/VXv/r0r/bK9wIIR9wHm3yMr70VqlZI062JA64DWmt4O+6ueA96oPYkS1m0gidAVuglU38Rp2DKEQS/Uhm4aeeufE++cTVDRTN02f3CNxANrw6338ZHDmaKFOM5gJfAC4880XgaxMiuhjRHlxCmbfV+FiAceZSSIqyn6FaMtoMu/jgPLVPG6vMASQy4TpBnsJ+8bzdiXybAG6ZVtrDgo8jyG/MYHXzrKYdgGDVcTnopG3zQp4ZUQFqNlYMNghaHTtxh8x7+Mt9P3L7bkLGvNZSz+l3J7tyV+YUreg6+l9rI3hD6RX9dt/VstfEPK8nGnvrw8m+jweYVhYirofG9f17w4ijHCdzXMhIAkD7ZZ9/3OZK3226Eml/wvyrUwRg39ju2W9K3DLn4C9in568ZzO6pO7kPH8++MVVLkxxwVY5D7DnnzAUsfpe02SxXq/g10WMCOsMDWmL8MIfFNL3mMBCocFcD51xq7ziX8q1DVsTxy4khNc8t71a8UTVzI4rXw+Jx6cSaf9dC7nAoHnAPsIQtduQJpLtU1Y9lu7dDcLPvmoMd+4L8mnfZyn6FtA4kT1HTf025ybX1lhzFfASe7oY5j2oQaF0rX+fXpQfelj8t8+/E+vbR+2iy/1xpgPs7sY2E3w31oP889om3naeHUu4RuBCYSOsVTLqplwClzcNnuKhqylNG2Bc5UNKgTHN1OTBROED4H3f3FLj7JKr7NocL9PZLgjVC47vKdEc3UoZryn14TFCqr+fwlfra+hiD1hhwiA9GEhZH3hN3Z40hYCoTnpWPF45uFak/fBsXWbPDZNvf1IhJSUORavkNBjznqSf86/C5vyAkaAOUqN/PkD0cJTOqduYO7gEJKutLkqaY8yO9temW+MxsFsG2lr28R/aX71jGyNXELBpzqQw1vHWzlikQCny0eCJ5swWTPdZp//ng//ziH//nMj5lNZLA6B83OCRQcoThHy7GCGRadJT0q/RNLQl2fv0Q/LjPwTrjJFJIZWR6nhmK85NvrumKkx1XdKhChC9DlggcwAErYTRNKMNqsQCz7+uhpoo9FHi+ckIxpG0ihYrUyei20V6T22t/8nWyioNOdKqXyDmjPiqWh7gSDixF3Ql/6K9gL35fD/YdM/E67WH6ge1BnH/7VmgTLWHF/WrvE6pAjsrBPUFMDmoyY4bhPCWiFp7eFb8trlGFuncMIVpKcGwYvClEdDuQf6xLAX4Po1hlgyS7wTC79N7J5xmaXjyj4kah44AAAAAAAAAAAAA==);
    }
  
    .neterror-vnext .icon-thinking {
      content: url(data:image/webp;base64,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);
    }
  }
  
  @media (-ms-high-contrast: active) {
    .neterror-vnext .icon-disconnected {
      content: url(data:image/webp;base64,UklGRlYPAABXRUJQVlA4TEkPAAAv/8A/EH/CoJEkReVf7fE9M1hg2LaNI+4/7fW7r2bYto0j7j/t9buvZtBGkpBBASMFJ+Dg88rIO0DaoOAJJmmq7RiAjRBC+LF/HiG0J0AIceL4eQghDKXQ917jdY0659z+/97+/9kTQiks71ud0z0h1sqeMJyzxusae0Kslce3teb8PO+eEGsllMKefMv7uryv43Vdsdb2RIbjtpEcqaT8sx5XfeYfEROQ/83ctFjOsZZwtEuOrXCbccbKXD+pJj1loabsU2OvOeVa0QU85OnWBPLCrUCeH7pXdPwkvwN1Y3uZncu0TH01ZWnb68TR/0koaRxzaFqWl1lm93k8VVYfXOAQUz1m4dH9Xw/kCJKWiej/BHh3tr1tdNu26mk59Zxz7i3fxIveSZQlyLJKhj6qA2/n+R+PKJckG6je/0X0fwJoS9sep5F+9ez79C7hBEPEFiO/Lh3AVJzpoalspKZd3P/1IIzh4PdpRP8nQP4Cv652202xtPmmcf1RpM6vT3q5wTT0r10XVLVAlV1rAHjj5SsU8JRdYnCeuyv8ioB1fjk1N/yu9yjyS0oc2Z+7CzIsMkwW8B6h5XxsOKHOMIuJB5x5wjv3KDNMCux5RM9VQyjv5VitQtPMsuBKvWyGSYmBXpmoOcrkmGi0zEpclTLqHNthZNJI0thhm2Ni0DKXgJeEIsssRno1jPo3TJaJQTCN9EqzzrM1erzQqpn1NquVM2Rr1eQ3mjy8sIw2vNX+Zf38RvsML3nsEvDHN5tLkgf++baT/b9uDOVt50H/IwDfz6ZvvjlWccj72YJYmeGqnxWkSoasnwXaygSDXuB2m2JpFvrSmI/Fxla/C/pKD1Z7tS2MwvX5EteVKXb1rxvAUOkoRfX1xigA8zj0Xcvvt/51eD8DgNlUvyiDXEkUiqs3BsD0zTf8xX6YAOhH9yvGUCqRW7XZQgHTvuHvbfp3AEv7cwtMywJeadYA4WvDP7Htz8Di8WdK2kqGK5VZA0yef64/Adr+UA7vKgM4hdWfgMnzz25PwNL9QCCqeiKIvjcKZ8/jW5Z+sPIn6FMVM3U5g3Dgbbau93+5+M13mJLPcKWtncLU8lZtkH7w9PT0JVxrd5Si7E8IB97yyfXBe/+Bk6oNzHRVG8wtbztKbuC1GpyqnMap4Y2PugK9qg3MRNNO4ytvfdAMMNdqcJqqFA689V7zZMCp8gAzUbRV6HnrvZTSBHCVzD4SnKJ+gtDz1jt5OzI0QJhlahiLnn+k0PHWTyqZIYVsQMhfYSF6/oG8480Paq4p5GDZqMZvevqB3Hj7SaNlUsZyqnwxb7X0A7lxD7PSeaAdsetoQGV+UNLncuMhxuI2dLSzkfIY2WjpU82BB3mWh2uHeW+kx8aYDyr6gebAwxw0h2EItHm0PQJMCu3kgQd61WxtbiDNmNsJjwmkZTzUQZ5o83gqoWMbVJ08W1x4sBdpNM6SJzmgTB4d7NFgLmVXS5LNDJc4FiMPuM3ShauvWCbOA/wjgmCsTnBpowMfvUeRNDXe7x6u6pSxGO5fhzJltni7fyGolCnh7x9H2MzzKDKPQeXeETZd1niNgUeRLlu8xaAJi3TZYYgBJ9TJ4jBGYcBTsog6R+EFRboYNDFo8CFdCvgYMOh02WEg2Y7tnTsjXWpMJD2Od26ESxYxCBBKeXADbLqs0QGD0mPrsU0XhwwkDY9unS5iFIBSwkPzKBNmrR7o1b/Z6vcKEEp5s8lnSkCv5kEFS5+fKwOh+IPKJX3EwJM8qnlQSiCLiWRTPDwkd5IvWCeNGHiSvfqHVGaSPbZps8VEMpRij0iZ5ACbNJUCPMlZ0wOKGkgeUaVMpXDEmYSs9Hie1ZGcUCdMpdDziD0hysPD6ZVIzkpi7VyWDdx5KoWe7BAaoNfwcN7JyAYmRvZP//yO1bKYjgYdVQotcJUmgFnp0bhDehTxyQqAEE9te7decVguhu60SqEHTJISEOXhsZgmyD2eYuMKqLqpaP11t1kDFEPbrlLoCVwXHoCz8mNp1UD+BxeZUUl8NBvu6gjMBi0qhZ4EU3UAyOoeyjsZZNAS1wnV1nS9qysohqlKoefltaYGCK70SIoDPZZRsQviqznj/iFCGIpIpdDz0rRaDIgq9jieNQCPeIqJC8TGnPl5DWH4UaHn1WmlaAY4y8PDeKcInCERdYGqMeffrVm9Qc+rreolDhoABuW1bgx3ZZqBDh8i4gIMOuRY1FINXisd/1lgT8KkYaXXHO7prAY44SkeLkDUUVvqg6ol8os4FTpCmNXXuGq2O3IPwKwlmi4Au6O01E3VEvkiIhZzC5irrzHI7W5ajUCLZTTsEojmoGfqwSsl8qVcrjEHwFxdjYvc7sVlQIaLxgRgeyETq4OWJfLl0/USGcBcTY2Lyuk+Wo1A0lJiecPh64WcVjotS+TLp/UHjQDm6mq0Rf09mLsBWTYWjsPKXGisRS1L5MunG+sPNACYq69hrjEc76ozkPShRNKGxPpSrGK+KJHvnm7+1QfqAczV17BZbkczOYDrl7GYUH0+SrMwl6SyomLp2ojTGEhirr4GF6k/VnC1JHssJZIZ6e4oGTCXpBKpm0hwbcRpDCSYawo1Tq5sRxp0IdnOcLEIR/qjeMBckkqkNmZfEwZtxGkMBMIktxp2Ven2Sqe1Tg7JE0qJ5IhLa7AiSR5pzOGGcthGnMbI8iKPNWhdbrs0mlesFIP00BJJFy7ODWtf+gSd0hsYtpF6gRwALlK/gl2l0bZrVGLNXCdgO8PFYs7x9ijyxgBS1voD3LSR+qPcAKJrtBqcXOpto0YlUg2uC8ATSomko+XzDvll8lsk5Wly3fwAN21EvpAbgGV5WoHW5aNt0ahEqmHWBWCAkVjO28TtHKD1mzZ8rbhp9fSFSsfyIvVr0Lo0plc1KpFqmHUFOEG7WNjQJmw3LuCyi+bAH2/6iaR+gbnc1qB1yV/iTY1KpBpmnEiyDcpJLHNa+16cd9EIf7zhJyon12wAYZBGW4N0LZJPXQqL2KtEqmHWiSTbGTuJZmg3blZWOO+iEX575K1KJFzlDUtzeXMDcLq6lqVIKpFqmHUlyXZGKdHMaN9tpmaFYRcNfO8Sb02JQJI0BJZnlze3APH0MuV5zmMbqNqsCyTbGaXEc35C3M7DSvBd1BOciLw1+wiQJcltgV0lP930enNdgGxnlBLRcAKlMw0rpH3UsbTy1uxXAEn1wVjaVfJmO3NdAHYzSoloxqljd+pXKPtoxeyt2a9YzivyZgF2lby3bcx1AegC1hLT6UnpDOpXxp2aWJv9isNWq0XKtgC7upQbe11yXQBOAVuJ6vKkUHbQaIeQq0SqvtLE+L/B2F6Q7CcA55dTuCF0WTiQ5BvUTqJqOX3YQ94AwfdSiVR71ZuIlw8aGNsrZNtPkFTyNPYv4+SSckeSe6hK4pp1kHaRSh6L9i6RqqneRLyIyFYDY3vlMvXTrLpPXeBygK4ksr4D8j5HLJH6tdZEvKS3GpjevlMNlswCq0doJ7EtumjvrETqraoe8dLSGmAe/Q/c7s/QTqK77CKU+4rUrVTc8NLePWhgHl/b14Q0AUUt0bV02t/VyKpr6YaX0+2DBuBTf0oWwOzUTUUwViI86CaUe0orvZZu/E26rTYf39Pt739hJcpZN/T3FGqdlk3Ey47OboqlMWa53OycxDrvKJS7i1o2ES/a9R1xvqO0iGXRRLxojXw/GYhFkprIreh3npiH16X7mQOnIkkeobRaUn4dw92cSFpmY1PjFRfKvbhhp76LsDUNpdUb7b2o9AaENBtjaryS3LcgHye3p6vfIMmzFy0bSvX4c4RyGAM4l1tuXTPU0Vw2IR3FqZpvsqPQTp54p7AJw0EUKoR5C7MmU851YpRtw3yQVCP4FlumynGJTqeNrBwjr2Blgz2lcmziWd1GpGOoW6HfwKzJdCPhwDRuxfkYxVZC2WDLVDmLA4pvxnAIudUYNigE5YwT7xQ2Ix9CbrV2AyWcbrJEp2a7MB9Cpak8b9Ex1o1NJI3bYX4IyRsIeYuJmW6kWFDKDpgfQ5IXbVkIyvGVQWkHzI+ydUQ5WSVp2APzu7rD6Ua+X1BK2APze6q5Uo5PbEy3C+Z3tCFXTpaoTN4H8/vZMlaOFAe8KO1DmO/mAa+dPLFW3gmGN4stD8hKe3G5k61+xCdMvhunchcbcvXY8oBB3W6Y30NNph7xiVCK7UYY7mDNQD+2POCsvB+05XBVKQoeJ8jqDoD5wXYUGpIiYaXEA8DlWDVDFQ0SJHk4AvbuSBGnIvEJLsqHgNYP88BMlLysMGk4BuFykCbitOS+r4RZ/THAroeomYqav6pgrv4gYNf9vhKsmkasmqs/CtjV9/lK6UTLDixWMNdwGKDN2+3vKQeiZRdgLrGCubIdB6ybt3mIBCdqnkMvuVUIk9wOBFg7+Sv8EiA4UfMI7iXJrQIXqTvUMqTuZco55/GlNYDgRM0uEJuF3GqcXNkO9vrgRM9zeDT1ZgW7qvR39a0VPV/DvUlf4PsatC5v7ufLX4uiv8O89grB+SPErTFNfZj2uWrlRdN/gl7VfQQnkpcpiI/GeGMHCH2RiS3KTFT9Hab6fzAWEXHhCMRHSeNpn9BmqVwqjhdOVP0HuNYaKCTtj4G1LpWpiRvFLhcpd4Hj5ViU/Q3mtRW4I+KWx4D4Mksq+aVNthYstS+5SMqXxK2FE2U7aFV9AC9t89ACsHaaVfel6j62gZtDJuoeg9dWBNdKJA9tliG1/ZhzZZ7Gvo2BV5ZjUfiSqOoOvJych3a7h5EVhTsYajW400Ty4mKKTHSew1wpMJNu3Wh5AYW3ovUFpuoIWUci4vKiPEO5GFlRfOC51lDKeQejeVGeVC5no4Ho3sJQM27PlLTZde6To/x6YKUHZpArDuNL6KFj8MoEWS+bgqo92F62YFXrKKWXF6xriaKflVSp7afskdu+1tL3M+f/CSvDfibyxgjQ/etvtqd93vM8wbufPfX1DzuG3k7jj99sf245+X7cF9n26xeGph9fTLb9dNcE9mOjsu3bqjuzHznZTLsGP13sTZ7ZkPBnNsFm2Q2JJpAHk2MupDh78rzLsBw2RIe+B6/q/ArEHaFAcIPHZXZl8O8OSoCzG5t5nVtTeNrBHIFLJrv/XWYVFB92MDasHnSdV4HZx1ewUGteJ2Wz61NTAcQ8nr4Fs6slr68X7vP3b1Q8//eHn3xQ1pLrztla/iYfAA==);
    }
  
    .neterror-vnext .icon-thinking {
      content: url(data:image/webp;base64,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);
    }
  }
  </style>
		<script>(function(){function l(a,b,c){return Function.prototype.call.apply(Array.prototype.slice,arguments)}function m(a,b,c){var e=l(arguments,2);return function(){return b.apply(a,e)}}function n(a,b){var c=new p(b);for(c.h=[a];c.h.length;){var e=c,d=c.h.shift();e.i(d);for(d=d.firstChild;d;d=d.nextSibling)1==d.nodeType&&e.h.push(d);}}function p(a){this.i=a;}function q(a){a.style.display="";}function r(a){a.style.display="none";}var t=/\s*;\s*/;function u(a,b){this.l.apply(this,arguments);}u.prototype.l=function(a,b){this.a||(this.a={});if(b){var c=this.a,e=b.a;for(d in e)c[d]=e[d];}else {var d=this.a;e=v;for(c in e)d[c]=e[c];}this.a.$this=a;this.a.$context=this;this.f="undefined"!=typeof a&&null!=a?a:"";b||(this.a.$top=this.f);};var v={$default:null},w=[];function x(a){for(var b in a.a)delete a.a[b];a.f=null;w.push(a);}function y(a,b,c){try{return b.call(c,a.a,a.f)}catch(e){return v.$default}}
  u.prototype.clone=function(a,b,c){if(0<w.length){var e=w.pop();u.call(e,a,this);a=e;}else a=new u(a,this);a.a.$index=b;a.a.$count=c;return a};var z;window.trustedTypes&&(z=trustedTypes.createPolicy("jstemplate",{createScript:function(a){return a}}));var A={};function B(a){if(!A[a])try{var b="(function(a_, b_) { with (a_) with (b_) return "+a+" })",c=window.trustedTypes?z.createScript(b):b;A[a]=window.eval(c);}catch(e){}return A[a]}
  function E(a){var b=[];a=a.split(t);for(var c=0,e=a.length;c<e;++c){var d=a[c].indexOf(":");if(!(0>d)){var g=a[c].substr(0,d).replace(/^\s+/,"").replace(/\s+$/,"");d=B(a[c].substr(d+1));b.push(g,d);}}return b}function F(){}var G=0,H={0:{}},I={},J={},K=[];function L(a){a.__jstcache||n(a,function(b){M(b);});}var N=[["jsselect",B],["jsdisplay",B],["jsvalues",E],["jsvars",E],["jseval",function(a){var b=[];a=a.split(t);for(var c=0,e=a.length;c<e;++c)if(a[c]){var d=B(a[c]);b.push(d);}return b}],["transclude",function(a){return a}],["jscontent",B],["jsskip",B]];
  function M(a){if(a.__jstcache)return a.__jstcache;var b=a.getAttribute("jstcache");if(null!=b)return a.__jstcache=H[b];b=K.length=0;for(var c=N.length;b<c;++b){var e=N[b][0],d=a.getAttribute(e);J[e]=d;null!=d&&K.push(e+"="+d);}if(0==K.length)return a.setAttribute("jstcache","0"),a.__jstcache=H[0];var g=K.join("&");if(b=I[g])return a.setAttribute("jstcache",b),a.__jstcache=H[b];var h={};b=0;for(c=N.length;b<c;++b){d=N[b];e=d[0];var f=d[1];d=J[e];null!=d&&(h[e]=f(d));}b=""+ ++G;a.setAttribute("jstcache",
  b);H[b]=h;I[g]=b;return a.__jstcache=h}function P(a,b){a.j.push(b);a.o.push(0);}function Q(a){return a.c.length?a.c.pop():[]}
  F.prototype.g=function(a,b){var c=R(b),e=c.transclude;if(e)(c=S(e))?(b.parentNode.replaceChild(c,b),e=Q(this),e.push(this.g,a,c),P(this,e)):b.parentNode.removeChild(b);else if(c=c.jsselect){c=y(a,c,b);var d=b.getAttribute("jsinstance");var g=!1;d&&("*"==d.charAt(0)?(d=parseInt(d.substr(1),10),g=!0):d=parseInt(d,10));var h=null!=c&&"object"==typeof c&&"number"==typeof c.length;e=h?c.length:1;var f=h&&0==e;if(h)if(f)d?b.parentNode.removeChild(b):(b.setAttribute("jsinstance","*0"),r(b));else if(q(b),
  null===d||""===d||g&&d<e-1){g=Q(this);d=d||0;for(h=e-1;d<h;++d){var k=b.cloneNode(!0);b.parentNode.insertBefore(k,b);T(k,c,d);f=a.clone(c[d],d,e);g.push(this.b,f,k,x,f,null);}T(b,c,d);f=a.clone(c[d],d,e);g.push(this.b,f,b,x,f,null);P(this,g);}else d<e?(g=c[d],T(b,c,d),f=a.clone(g,d,e),g=Q(this),g.push(this.b,f,b,x,f,null),P(this,g)):b.parentNode.removeChild(b);else null==c?r(b):(q(b),f=a.clone(c,0,1),g=Q(this),g.push(this.b,f,b,x,f,null),P(this,g));}else this.b(a,b);};
  F.prototype.b=function(a,b){var c=R(b),e=c.jsdisplay;if(e){if(!y(a,e,b)){r(b);return}q(b);}if(e=c.jsvars)for(var d=0,g=e.length;d<g;d+=2){var h=e[d],f=y(a,e[d+1],b);a.a[h]=f;}if(e=c.jsvalues)for(d=0,g=e.length;d<g;d+=2)if(f=e[d],h=y(a,e[d+1],b),"$"==f.charAt(0))a.a[f]=h;else if("."==f.charAt(0)){f=f.substr(1).split(".");for(var k=b,O=f.length,C=0,U=O-1;C<U;++C){var D=f[C];k[D]||(k[D]={});k=k[D];}k[f[O-1]]=h;}else f&&("boolean"==typeof h?h?b.setAttribute(f,f):b.removeAttribute(f):b.setAttribute(f,""+h));
  if(e=c.jseval)for(d=0,g=e.length;d<g;++d)y(a,e[d],b);e=c.jsskip;if(!e||!y(a,e,b))if(c=c.jscontent){if(c=""+y(a,c,b),b.innerHTML!=c){for(;b.firstChild;)e=b.firstChild,e.parentNode.removeChild(e);b.appendChild(this.m.createTextNode(c));}}else {c=Q(this);for(e=b.firstChild;e;e=e.nextSibling)1==e.nodeType&&c.push(this.g,a,e);c.length&&P(this,c);}};function R(a){if(a.__jstcache)return a.__jstcache;var b=a.getAttribute("jstcache");return b?a.__jstcache=H[b]:M(a)}
  function S(a,b){var c=document;if(b){var e=c.getElementById(a);if(!e){e=b();var d=c.getElementById("jsts");d||(d=c.createElement("div"),d.id="jsts",r(d),d.style.position="absolute",c.body.appendChild(d));var g=c.createElement("div");d.appendChild(g);g.innerHTML=e;e=c.getElementById(a);}c=e;}else c=c.getElementById(a);return c?(L(c),c=c.cloneNode(!0),c.removeAttribute("id"),c):null}function T(a,b,c){c==b.length-1?a.setAttribute("jsinstance","*"+c):a.setAttribute("jsinstance",""+c);}window.jstGetTemplate=S;window.JsEvalContext=u;window.jstProcess=function(a,b){var c=new F;L(b);c.m=b?9==b.nodeType?b:b.ownerDocument||document:document;var e=m(c,c.g,a,b),d=c.j=[],g=c.o=[];c.c=[];e();for(var h,f,k;d.length;)h=d[d.length-1],e=g[g.length-1],e>=h.length?(e=c,f=d.pop(),f.length=0,e.c.push(f),g.pop()):(f=h[e++],k=h[e++],h=h[e++],g[g.length-1]=e,f.call(c,k,h));};
  })();
  
  // Copyright 2017 The Chromium Authors
  // Copyright (C) Microsoft Corporation. All rights reserved.
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  
  
  const HIDDEN_CLASS$1 = 'hidden';
  
  // 
  
  //
  
  // Copyright 2015 The Chromium Authors
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  
  
  let mobileNav = false;
  
  /**
   * For small screen mobile the navigation buttons are moved
   * below the advanced text.
   */
  function onResize() {
    const helpOuterBox = document.querySelector('#details');
    const mainContent = document.querySelector('#main-content');
    const mediaQuery = '(min-width: 240px) and (max-width: 420px) and ' +
        '(min-height: 401px), ' +
        '(max-height: 560px) and (min-height: 240px) and ' +
        '(min-width: 421px)';
  
  /**
   * The #details section queried in |helpOuterBox| does not exist in case of the
   * Elixir revamped error pages (msElixirNetworkErrorPages).
   */
    if (!helpOuterBox) {
      return;
    }
  
    const detailsHidden = helpOuterBox.classList.contains(HIDDEN_CLASS$1);
    const runnerContainer = document.querySelector('.runner-container');
  
    // Check for change in nav status.
    if (mobileNav !== window.matchMedia(mediaQuery).matches) {
      mobileNav = !mobileNav;
  
      // Handle showing the top content / details sections according to state.
      if (mobileNav) {
        mainContent.classList.toggle(HIDDEN_CLASS$1, !detailsHidden);
        helpOuterBox.classList.toggle(HIDDEN_CLASS$1, detailsHidden);
        if (runnerContainer) {
          runnerContainer.classList.toggle(HIDDEN_CLASS$1, !detailsHidden);
        }
      } else if (!detailsHidden) {
        // Non mobile nav with visible details.
        mainContent.classList.remove(HIDDEN_CLASS$1);
        helpOuterBox.classList.remove(HIDDEN_CLASS$1);
        if (runnerContainer) {
          runnerContainer.classList.remove(HIDDEN_CLASS$1);
        }
      }
    }
  }
  
  function setupMobileNav() {
    window.addEventListener('resize', onResize);
    onResize();
  }
  
  document.addEventListener('DOMContentLoaded', setupMobileNav);
  
  // Copyright 2022 The Chromium Authors
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  /**
   * Verify |value| is truthy.
   * @param value A value to check for truthiness. Note that this
   *     may be used to test whether |value| is defined or not, and we don't want
   *     to force a cast to boolean.
   */
  function assert(value, message) {
      if (value) {
          return;
      }
      throw new Error('Assertion failed' + (message ? `: ${message}` : ''));
  }
  
  // Copyright 2022 The Chromium Authors
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  /**
   * @fileoverview This file defines a singleton which provides access to all data
   * that is available as soon as the page's resources are loaded (before DOM
   * content has finished loading). This data includes both localized strings and
   * any data that is important to have ready from a very early stage (e.g. things
   * that must be displayed right away).
   *
   * Note that loadTimeData is not guaranteed to be consistent between page
   * refreshes (https://crbug.com/740629) and should not contain values that might
   * change if the page is re-opened later.
   */
  class LoadTimeData {
      data_ = null;
      /**
       * Sets the backing object.
       *
       * Note that there is no getter for |data_| to discourage abuse of the form:
       *
       *     var value = loadTimeData.data()['key'];
       */
      set data(value) {
          assert(!this.data_, 'Re-setting data.');
          this.data_ = value;
      }
      /**
       * @param id An ID of a value that might exist.
       * @return True if |id| is a key in the dictionary.
       */
      valueExists(id) {
          // TODO(42630414): Re-add assert check.
          // Commenting assert statement to mitigate Bug 42601651.
          // assert(this.data_, 'No data. Did you remember to include strings.js?');
          return this.data_ ? id in this.data_ : false;
      }
      /**
       * Fetches a value, expecting that it exists.
       * @param id The key that identifies the desired value.
       * @return The corresponding value.
       */
      getValue(id) {
          assert(this.data_, 'No data. Did you remember to include strings.js?');
          const value = this.data_[id];
          assert(typeof value !== 'undefined', 'Could not find value for ' + id);
          return value;
      }
      /**
       * As above, but also makes sure that the value is a string.
       * @param id The key that identifies the desired string.
       * @return The corresponding string value.
       */
      getString(id) {
          const value = this.getValue(id);
          assert(typeof value === 'string', `[${value}] (${id}) is not a string`);
          return value;
      }
      /**
       * Returns a formatted localized string where $1 to $9 are replaced by the
       * second to the tenth argument.
       * @param id The ID of the string we want.
       * @param args The extra values to include in the formatted output.
       * @return The formatted string.
       */
      getStringF(id, ...args) {
          const value = this.getString(id);
          if (!value) {
              return '';
          }
          return this.substituteString(value, ...args);
      }
      /**
       * Returns a formatted localized string where $1 to $9 are replaced by the
       * second to the tenth argument. Any standalone $ signs must be escaped as
       * $$.
       * @param label The label to substitute through. This is not an resource ID.
       * @param args The extra values to include in the formatted output.
       * @return The formatted string.
       */
      substituteString(label, ...args) {
          return label.replace(/\$(.|$|\n)/g, function (m) {
              assert(m.match(/\$[$1-9]/), 'Unescaped $ found in localized string.');
              if (m === '$$') {
                  return '$';
              }
              const substitute = args[Number(m[1]) - 1];
              if (substitute === undefined || substitute === null) {
                  // Not all callers actually provide values for all substitutes. Return
                  // an empty value for this case.
                  return '';
              }
              return substitute.toString();
          });
      }
      /**
       * Returns a formatted string where $1 to $9 are replaced by the second to
       * tenth argument, split apart into a list of pieces describing how the
       * substitution was performed. Any standalone $ signs must be escaped as $$.
       * @param label A localized string to substitute through.
       *     This is not an resource ID.
       * @param args The extra values to include in the formatted output.
       * @return The formatted string pieces.
       */
      getSubstitutedStringPieces(label, ...args) {
          // Split the string by separately matching all occurrences of $1-9 and of
          // non $1-9 pieces.
          const pieces = (label.match(/(\$[1-9])|(([^$]|\$([^1-9]|$))+)/g) ||
              []).map(function (p) {
              // Pieces that are not $1-9 should be returned after replacing $$
              // with $.
              if (!p.match(/^\$[1-9]$/)) {
                  assert((p.match(/\$/g) || []).length % 2 === 0, 'Unescaped $ found in localized string.');
                  return { value: p.replace(/\$\$/g, '$'), arg: null };
              }
              // Otherwise, return the substitution value.
              const substitute = args[Number(p[1]) - 1];
              if (substitute === undefined || substitute === null) {
                  // Not all callers actually provide values for all substitutes. Return
                  // an empty value for this case.
                  return { value: '', arg: p };
              }
              return { value: substitute.toString(), arg: p };
          });
          return pieces;
      }
      /**
       * As above, but also makes sure that the value is a boolean.
       * @param id The key that identifies the desired boolean.
       * @return The corresponding boolean value.
       */
      getBoolean(id) {
          const value = this.getValue(id);
          assert(typeof value === 'boolean', `[${value}] (${id}) is not a boolean`);
          return value;
      }
      /**
       * As above, but also makes sure that the value is an integer.
       * @param id The key that identifies the desired number.
       * @return The corresponding number value.
       */
      getInteger(id) {
          const value = this.getValue(id);
          assert(typeof value === 'number', `[${value}] (${id}) is not a number`);
          assert(value === Math.floor(value), 'Number isn\'t integer: ' + value);
          return value;
      }
      /**
       * Override values in loadTimeData with the values found in |replacements|.
       * @param replacements The dictionary object of keys to replace.
       */
      overrideValues(replacements) {
          assert(typeof replacements === 'object', 'Replacements must be a dictionary object.');
          assert(this.data_, 'Data must exist before being overridden');
          for (const key in replacements) {
              this.data_[key] = replacements[key];
          }
      }
      /**
       * Reset loadTimeData's data. Should only be used in tests.
       * @param newData The data to restore to, when null restores to unset state.
       */
      resetForTesting(newData = null) {
          this.data_ = newData;
      }
      /**
       * @return Whether loadTimeData.data has been set.
       */
      isInitialized() {
          return this.data_ !== null;
      }
  }
  const loadTimeData = new LoadTimeData();
  // Edge only
  // Guard against overriding existing loadTimeData. This could happen if either:
  // a) the page is already including loadTimeData from a script tag (perhaps it
  //    is still using the deprecated version) but then also ends up including
  //    this file as part of some other dependency, or
  // b) the page is using multiple webpack entry points (not a good idea anyway)
  //    that both include this file.
  // In either case, we should warn the developer that something is wrong and not
  // silently overwrite the existing instance which might already be initialized
  // with data.
  console.assert(!window.hasOwnProperty('loadTimeData'), 'window.loadTimeData is already set.');
  Object.assign(window, { loadTimeData: loadTimeData });
  
  // Copyright 2023 The Chromium Authors
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  
  const HIDDEN_CLASS = 'hidden';
  
  // Copyright 2014 The Chromium Authors
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  
  
  /** @const */
  document.querySelector('html').dir == 'rtl';
  
  // Copyright 2013 The Chromium Authors. All rights reserved.
  // Copyright (C) Microsoft Corporation. All rights reserved.
  // Use of this source code is governed by a BSD-style license that can be
  // found in the LICENSE file.
  
  
  function toggleHelpBox() {
    const helpBoxOuter = document.getElementById('details');
    helpBoxOuter.classList.toggle(HIDDEN_CLASS);
    const detailsButton = document.getElementById('details-button');
    if (helpBoxOuter.classList.contains(HIDDEN_CLASS)) {
      detailsButton.innerText = detailsButton.detailsText;
      detailsButton.classList.remove('expanded');
    } else {
      detailsButton.innerText = detailsButton.hideDetailsText;
      detailsButton.classList.add('expanded');
    }
  
    // Details appears over the main content on small screens.
    if (mobileNav) {
      document.getElementById('main-content').classList.toggle(HIDDEN_CLASS);
      const runnerContainer = document.querySelector('.runner-container');
      if (runnerContainer) {
        runnerContainer.classList.toggle(HIDDEN_CLASS);
      }
    }
  }
  
  function diagnoseErrors() {
    // 
    if (window.errorPageController) {
      window.errorPageController.diagnoseErrorsButtonClick();
    }
    // 
    // 
  }
  
  // Subframes use a different layout but the same html file.  This is to make it
  // easier to support platforms that load the error page via different
  // mechanisms (Currently just iOS). We also use the subframe style for portals
  // as they are embedded like subframes and can't be interacted with by the user.
  if (window.top.location != window.location || window.portalHost) {
    document.documentElement.setAttribute('subframe', '');
  }
  
  // Re-renders the error page using |strings| as the dictionary of values.
  // Used by NetErrorTabHelper to update DNS error pages with probe results.
  function updateForDnsProbe(strings) {
    const context = new JsEvalContext(strings);
    jstProcess(context, document.body);
  }
  
  // Given the classList property of an element, adds an icon class to the list
  // and removes the previously-
  function updateIconClass(classList, newClass) {
    let oldClass;
  
    if (classList.hasOwnProperty('last_icon_class')) {
      oldClass = classList['last_icon_class'];
      if (oldClass == newClass) {
        return;
      }
    }
  
    classList.add(newClass);
    if (oldClass !== undefined) {
      classList.remove(oldClass);
    }
  
    classList['last_icon_class'] = newClass;
  
    document.body.classList.add('neterror');
  }
  
  // Does a search using |baseSearchUrl| and the text in the search box.
  function search(baseSearchUrl) {
    const searchTextNode = document.getElementById('search-box');
    document.location = baseSearchUrl + searchTextNode.value;
    return false;
  }
  
  // Called when an <a> tag generated by the navigation correction service is
  // clicked.
  // @param {{clickData: string}} jstdata
  function navigationCorrectionClicked(jstdata) {
    if (jstdata.clickData !== undefined && errorPageController) {
      window.errorPageController.edgeNavigationCorrectionClicked(jstdata.clickData);
    }
  }
  
  // Implements button clicks.  This function is needed during the transition
  // between implementing these in trunk chromium and implementing them in
  // iOS.
  function reloadButtonClick(url) {
    if (window.errorPageController) {
      window.errorPageController.reloadButtonClick();
    } else {
      location = url;
    }
  }
  
  function showSavedCopyButtonClick() {
    if (window.errorPageController) {
      window.errorPageController.showSavedCopyButtonClick();
    }
  }
  
  function downloadButtonClick() {
    if (window.errorPageController) {
      window.errorPageController.downloadButtonClick();
      const downloadButton = document.getElementById('download-button');
      downloadButton.disabled = true;
      downloadButton.textContent = downloadButton.disabledText;
  
      document.getElementById('download-link-wrapper')
        .classList.add(HIDDEN_CLASS);
      document.getElementById('download-link-clicked-wrapper')
        .classList.remove(HIDDEN_CLASS);
    }
  }
  
  function detailsButtonClick() {
    if (window.errorPageController) {
      window.errorPageController.detailsButtonClick();
    }
  }
  
  function toggleErrorInformationPopup() {
    document.getElementById('error-information-popup-container')
      .classList.toggle(HIDDEN_CLASS);
  }
  
  function launchOfflineItem(itemID, name_space) {
    window.errorPageController.launchOfflineItem(itemID, name_space);
  }
  
  function launchDownloadsPage() {
    window.errorPageController.launchDownloadsPage();
  }
  
  // Populates a summary of suggested offline content.
  function offlineContentSummaryAvailable(summary) {
    // Note: See AvailableContentSummaryToValue in
    // available_offline_content_helper.cc for the data contained in |summary|.
    if (!summary || summary.total_items == 0 ||
      !loadTimeData.valueExists('offlineContentSummary')) {
      return;
    }
    // TODO(https://crbug.com/852872): Customize presented icons based on the
    // types of available offline content.
    document.getElementById('offline-content-summary').hidden = false;
  }
  
  function getIconForSuggestedItem(item) {
    // Note: |item.content_type| contains the enum values from
    // chrome::mojom::AvailableContentType.
    switch (item.content_type) {
      case 1:  // kVideo
        return 'image-video';
      case 2:  // kAudio
        return 'image-music-note';
      case 0:  // kPrefetchedPage
      case 3:  // kOtherPage
        return 'image-earth';
    }
    return 'image-file';
  }
  
  function getSuggestedContentDiv(item, index) {
    // Note: See AvailableContentToValue in available_offline_content_helper.cc
    // for the data contained in an |item|.
    // TODO(carlosk): Present |snippet_base64| when that content becomes
    // available.
    let visual = '';
    const extraContainerClasses = [];
    // html_inline.py will try to replace src attributes with data URIs using a
    // simple regex. The following is obfuscated slightly to avoid that.
    const src = 'src';
    if (item.thumbnail_data_uri) {
      extraContainerClasses.push('suggestion-with-image');
      visual = `<img ${src}="${item.thumbnail_data_uri}">`;
    } else {
      extraContainerClasses.push('suggestion-with-icon');
      iconClass = getIconForSuggestedItem(item);
      visual = `<div><img class="${iconClass}"></div>`;
    }
  
    if (!item.attribution_base64) {
      extraContainerClasses.push('no-attribution');
    }
  
    return `
      <div class="offline-content-suggestion ${extraContainerClasses.join(' ')}"
        onclick="launchOfflineItem('${item.ID}', '${item.name_space}')">
          <div class="offline-content-suggestion-texts">
            <div id="offline-content-suggestion-title-${index}"
                 class="offline-content-suggestion-title">
            </div>
            <div class="offline-content-suggestion-attribution-freshness">
              <div id="offline-content-suggestion-attribution-${index}"
                   class="offline-content-suggestion-attribution">
              </div>
              <div class="offline-content-suggestion-freshness">
                ${item.date_modified}
              </div>
              <div class="offline-content-suggestion-pin-spacer"></div>
              <div class="offline-content-suggestion-pin"></div>
            </div>
          </div>
          <div class="offline-content-suggestion-visual">
            ${visual}
          </div>
      </div>`;
  }
  
  // Populates a list of suggested offline content.
  // Note: For security reasons all content downloaded from the web is considered
  // unsafe and must be securely handled to be presented on the dino page. Images
  // have already been safely re-encoded but textual content -- like title and
  // attribution -- must be properly handled here.
  function offlineContentAvailable(suggestions) {
    if (!suggestions || !loadTimeData.valueExists('offlineContentList')) {
      return;
    }
  
    const suggestionsHTML = [];
    for (let index = 0; index < suggestions.length; index++) {
      suggestionsHTML.push(getSuggestedContentDiv(suggestions[index], index));
    }
  
    document.getElementById('offline-content-suggestions').innerHTML =
      suggestionsHTML.join('\n');
  
    // Sets textual web content using |textContent| to make sure it's handled as
    // plain text.
    for (let index = 0; index < suggestions.length; index++) {
      document.getElementById(`offline-content-suggestion-title-${index}`)
        .textContent = atob(suggestions[index].title_base64);
      document.getElementById(`offline-content-suggestion-attribution-${index}`)
        .textContent = atob(suggestions[index].attribution_base64);
    }
  
    const contentListElement = document.getElementById('offline-content-list');
    if (document.dir == 'rtl') {
      contentListElement.classList.add('is-rtl');
    }
    contentListElement.hidden = false;
  }
  
  function onDocumentLoad() {
    // `loadTimeDataRaw` is injected to the `window` scope from C++.
    loadTimeData.data = window.loadTimeDataRaw;
    jstProcess(new JsEvalContext(window.loadTimeDataRaw), document.body);
  
    const showSearchBox = loadTimeData.valueExists('edge_vnext') && loadTimeData.getValue('edge_vnext').showSearchBox;
    if(showSearchBox) {
      document.body.classList.add('neterror-vnext');
      const bingSearchDiv = document.getElementById('neterror-bing-search');
      bingSearchDiv.classList.toggle(HIDDEN_CLASS);
    }
  
    const controlButtonDiv = document.getElementById('control-buttons');
    const reloadButton = document.getElementById('reload-button');
    const detailsButton = document.getElementById('details-button');
    const showSavedCopyButton = document.getElementById('show-saved-copy-button');
    const downloadButton = document.getElementById('download-button');
    const diagnoseButton = document.getElementById('diagnose-button');
    // needed for experiment
    const secondaryReloadButton = document.getElementById('secondary-reload-button');
    const gameButton = document.getElementById('game-button');
    const gameButtonContainer = document.getElementById('game-buttons');
  
    const reloadButtonVisible = loadTimeData.valueExists('reloadButton') &&
      loadTimeData.getValue('reloadButton').msg;
    const showSavedCopyButtonVisible =
      loadTimeData.valueExists('showSavedCopyButton') &&
      loadTimeData.getValue('showSavedCopyButton').msg;
    const downloadButtonVisible =
      loadTimeData.valueExists('downloadButton') &&
      loadTimeData.getValue('downloadButton').msg;
    const diagnoseButtonVisible =
      loadTimeData.valueExists('diagnoseButton') &&
      loadTimeData.getValue('diagnoseButton').msg;
    const gameButtonDisabled =
      loadTimeData.valueExists('disabledGame') &&
      loadTimeData.getBoolean('disabledGame');
  
    if (gameButtonDisabled) {
      gameButton.disabled = true;
      const managedIcon = gameButtonContainer.getElementsByClassName('managed-icon')[0];
      if (!!managedIcon && loadTimeData.valueExists('playGameMsg')) {
        managedIcon.setAttribute('title', loadTimeData.getString('disabledGameMsg'));
      }
    }
  
    // If Automatic HTTPS suggestions are defined, show messages.
    const automaticHTTPSVisible =
      loadTimeData.valueExists('httpsUpgradesMessage');
    if (automaticHTTPSVisible) {
      document.getElementById('https-upgrades-message')
        .classList.toggle(HIDDEN_CLASS);
      document.getElementById('https-upgrades-message-details')
        .classList.toggle(HIDDEN_CLASS);
    }
  
    // If offline content suggestions will be visible, the usual buttons will not
    // be presented.
    const offlineContentVisible =
      loadTimeData.valueExists('suggestedOfflineContentPresentationMode');
    if (offlineContentVisible) {
      document.querySelector('.nav-wrapper').classList.add(HIDDEN_CLASS);
      detailsButton.classList.add(HIDDEN_CLASS);
  
      if (downloadButtonVisible) {
        document.getElementById('download-link').hidden = false;
      }
  
      document.getElementById('download-links-wrapper')
        .classList.remove(HIDDEN_CLASS);
      document.getElementById('error-information-popup-container')
        .classList.add('use-popup-container', HIDDEN_CLASS);
      document.getElementById('error-information-button')
        .classList.remove(HIDDEN_CLASS);
  
      return;
    }
  
    let primaryButton;
    let secondaryButton;
    if (showSavedCopyButton.primary) {
      primaryButton = showSavedCopyButton;
      secondaryButton = reloadButton;
    } else {
      primaryButton = reloadButton;
      secondaryButton = showSavedCopyButton;
    }
  
    // Sets up the proper button layout for the current platform.
    {
      buttons.classList.add('suggested-left');
      controlButtonDiv.insertBefore(secondaryButton, primaryButton);
    }
  
    if (reloadButton.style.display == 'none' &&
      showSavedCopyButton.style.display == 'none' &&
      downloadButton.style.display == 'none' &&
      diagnoseButton.style.display == 'none') {
      detailsButton.classList.add('singular');
    }
  
    // Show control buttons.
    if (reloadButtonVisible || showSavedCopyButtonVisible ||
      downloadButtonVisible || diagnoseButtonVisible) {
      controlButtonDiv.hidden = false;
  
      // Set the secondary button state in the cases of two call to actions.
      if ((reloadButtonVisible || downloadButtonVisible) &&
        showSavedCopyButtonVisible) {
        secondaryButton.classList.add('secondary-button');
      }
  
      // Fix secondary button CSS.
      if (reloadButtonVisible && diagnoseButtonVisible) {
        reloadButton.classList.toggle(HIDDEN_CLASS);
        secondaryReloadButton.classList.toggle(HIDDEN_CLASS);
      }
    }
  }
  
  function launchGame() {
    const gameButtonDisabled =
      loadTimeData.valueExists('disabledGame') &&
      loadTimeData.getBoolean('disabledGame');
    if (!gameButtonDisabled) {
      // 
  
      // 
      window.errorPageController.openSurfGame();
      // 
    }
  }
  
  // Opens edge://settings/privacy.
  function launchEdgePrivacySettings() {
    window.errorPageController.openEdgePrivacySettings();
  }
  
  // Updates https_upgrade_state from
  // third_party/blink/public/mojom/renderer_preferences.mojom to
  // edge_https::UpgradeState::UPGRADE_FAILURE_IGNORED if Edge's
  // Automatic HTTPS component needs to be bypassed.
  function updateHttpsUpgradeState() {
    window.errorPageController.bypassEdgeHttpsUpgrades();
  }
  
  function bingSearchClick() {
    const value = document.getElementById('bing-input').value;
    if (!value) {
      return;
    }
    window.location.href = `https://www.bing.com/search?q=${encodeURIComponent(value)}&form=NETREL`;
  }
  
  function handleKeyDown(event) {
    if (event.key === 'Enter') {
      bingSearchClick();
    }
  }
  
  function handleTopSiteClick(url) {
    window.open(url);
  }
  
  function handleTopSiteKeydown(event, url) {
    if (event.key === 'Enter') {
      handleTopSiteClick(url);
    }
  }
  
  // Expose methods that are triggered either
  //  - By `onclick=...` handlers in the HTML code, OR
  //  - By `href="javascript:..."` in localized links.
  //  - By inected JS code coming from C++
  //
  //  since those need to be available on the 'window' object.
  Object.assign(window, {
    detailsButtonClick,
    diagnoseErrors,
    downloadButtonClick,
    launchDownloadsPage,
    reloadButtonClick,
    toggleErrorInformationPopup,
    toggleHelpBox,
    updateForDnsProbe,
    updateIconClass,
    search,
    navigationCorrectionClicked,
    reloadButtonClick,
    showSavedCopyButtonClick,
    downloadButtonClick,
    detailsButtonClick,
    toggleErrorInformationPopup,
    launchOfflineItem,
    launchDownloadsPage,
    offlineContentSummaryAvailable,
    getIconForSuggestedItem,
    getSuggestedContentDiv,
    offlineContentAvailable,
    launchGame,
    launchEdgePrivacySettings,
    updateHttpsUpgradeState,
    bingSearchClick,
    handleKeyDown,
    handleTopSiteClick,
    handleTopSiteKeydown,
  });
  
  document.addEventListener('DOMContentLoaded', onDocumentLoad);
  //# sourceMappingURL=edge-elixir-neterror.rollup.js.map
  </script>
		<style>/* Copyright (C) Microsoft Corporation. All rights reserved. */
  
  .msreadout-word-highlight:not(.msreadout-inactive-highlight) {
      background: #ffff00 !important;
      color: black !important;
  }
  
  .msreadout-line-highlight:not(.msreadout-inactive-highlight) {
      background: #b2d6f3 !important;
      color: black !important;
  }
  
  @media screen and (-ms-high-contrast: active) {
      .msreadout-word-highlight:not(.msreadout-inactive-highlight) {
          -ms-high-contrast-adjust: none;
          background-color: Highlight !important;
          color: HighlightText !important;
      }
  
      .msreadout-line-highlight:not(.msreadout-inactive-highlight) {
          -ms-high-contrast-adjust: none;
          background: yellow !important;
          color: black !important;
      }
  }
  /*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uLy4uLy4uL2Nzcy9yZWFkX291dF9sb3VkX3dlYi5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsOERBQThEOztBQUU5RDtJQUNJLDhCQUE4QjtJQUM5Qix1QkFBdUI7QUFDM0I7O0FBRUE7SUFDSSw4QkFBOEI7SUFDOUIsdUJBQXVCO0FBQzNCOztBQUVBO0lBQ0k7UUFDSSw4QkFBOEI7UUFDOUIsc0NBQXNDO1FBQ3RDLCtCQUErQjtJQUNuQzs7SUFFQTtRQUNJLDhCQUE4QjtRQUM5Qiw2QkFBNkI7UUFDN0IsdUJBQXVCO0lBQzNCO0FBQ0oiLCJzb3VyY2VzQ29udGVudCI6WyIvKiBDb3B5cmlnaHQgKEMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC4gKi9cclxuXHJcbi5tc3JlYWRvdXQtd29yZC1oaWdobGlnaHQ6bm90KC5tc3JlYWRvdXQtaW5hY3RpdmUtaGlnaGxpZ2h0KSB7XHJcbiAgICBiYWNrZ3JvdW5kOiAjZmZmZjAwICFpbXBvcnRhbnQ7XHJcbiAgICBjb2xvcjogYmxhY2sgIWltcG9ydGFudDtcclxufVxyXG5cclxuLm1zcmVhZG91dC1saW5lLWhpZ2hsaWdodDpub3QoLm1zcmVhZG91dC1pbmFjdGl2ZS1oaWdobGlnaHQpIHtcclxuICAgIGJhY2tncm91bmQ6ICNiMmQ2ZjMgIWltcG9ydGFudDtcclxuICAgIGNvbG9yOiBibGFjayAhaW1wb3J0YW50O1xyXG59XHJcblxyXG5AbWVkaWEgc2NyZWVuIGFuZCAoLW1zLWhpZ2gtY29udHJhc3Q6IGFjdGl2ZSkge1xyXG4gICAgLm1zcmVhZG91dC13b3JkLWhpZ2hsaWdodDpub3QoLm1zcmVhZG91dC1pbmFjdGl2ZS1oaWdobGlnaHQpIHtcclxuICAgICAgICAtbXMtaGlnaC1jb250cmFzdC1hZGp1c3Q6IG5vbmU7XHJcbiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogSGlnaGxpZ2h0ICFpbXBvcnRhbnQ7XHJcbiAgICAgICAgY29sb3I6IEhpZ2hsaWdodFRleHQgIWltcG9ydGFudDtcclxuICAgIH1cclxuXHJcbiAgICAubXNyZWFkb3V0LWxpbmUtaGlnaGxpZ2h0Om5vdCgubXNyZWFkb3V0LWluYWN0aXZlLWhpZ2hsaWdodCkge1xyXG4gICAgICAgIC1tcy1oaWdoLWNvbnRyYXN0LWFkanVzdDogbm9uZTtcclxuICAgICAgICBiYWNrZ3JvdW5kOiB5ZWxsb3cgIWltcG9ydGFudDtcclxuICAgICAgICBjb2xvcjogYmxhY2sgIWltcG9ydGFudDtcclxuICAgIH1cclxufSJdLCJzb3VyY2VSb290IjoiIn0= */</style>
	</head>

	<body style="font-family: 'Segoe UI',Arial,'Microsoft Yahei',sans-serif; font-size: 75%" jstcache="0" class="neterror">
		<div id="main-frame-error" class="interstitial-wrapper" jstcache="0">
			<div id="main-content" jstcache="0">
				<div class="icon icon-elixir-thinking" jseval="updateIconClass(this.classList, iconClass)" alt="" jstcache="1"></div>
				<div id="main-message" aria-live="assertive" aria-atomic="true" jstcache="0">
					<h1 jstcache="0">
						<span jsselect="heading" jsvalues=".innerHTML:msg" jstcache="14">嗯… 无法访问此页面</span>
						<a id="error-information-button" class="hidden" onclick="toggleErrorInformationPopup();" jstcache="0"></a>
					</h1>
					<p jsselect="summary" jsvalues=".innerHTML:msg" jstcache="2">你的网络由你所属的学校局域网决定，您当前的学校策略禁止或限制您访问这个网站。</p>
					<div id="https-upgrades-message" class="hidden" jstcache="0">
						<p id="https-upgrades-message-details" jsselect="httpsUpgradesMessage" jsvalues=".innerHTML:msg" class="hidden" jstcache="15" style="display: none;"></p>
					</div>
					<!--The suggestion list and error code are normally presented inline,
            in which case error-information-popup-* divs have no effect. When
            error-information-popup-container has the use-popup-container class, this
            information is provided in a popup instead.-->
					<div id="error-information-popup-container" jstcache="0">
						<div id="error-information-popup" jstcache="0">
							<div id="error-information-popup-box" jstcache="0">
								<div id="error-information-popup-content" jstcache="0">
									<div id="suggestions-list" style="" jsdisplay="(suggestionsSummaryList &amp;&amp; suggestionsSummaryList.length)" jstcache="26">
										<p jsvalues=".innerHTML:suggestionsSummaryListHeader" jstcache="28">请尝试：</p>
										<ul jsvalues=".className:suggestionsSummaryList.length == 1 ? 'single-suggestion' : ''" jstcache="29" class="">
											<li jsselect="suggestionsSummaryList" jsvalues=".innerHTML:summary" jstcache="31" jsinstance="1">向学校局域网策略管理者寻求帮助</li>
											<li jsselect="suggestionsSummaryList" jsvalues=".innerHTML:summary" jstcache="31" jsinstance="1">向该电脑的所有者或管理员寻求帮助</li>
											<li jsselect="suggestionsSummaryList" jsvalues=".innerHTML:summary" jstcache="31" jsinstance="1">更改网络或控制域</li>
										</ul>
										<p jsvalues=".innerHTML:suggestionsSummaryListHeader" jstcache="28">该网站禁止访问是由你的学校局域网策略管理者决定的，您目前的行动和访问记录均会由运营商提交至管理者，请您服从学校局域网策略</p>
									</div>
									<div class="error-code" jscontent="errorCode" jstcache="27">ERROR_SCHOOL_X_HOST</div>
									<p id="error-information-popup-close" jstcache="0">
										<a class="link-button" jscontent="closeDescriptionPopup" onclick="toggleErrorInformationPopup();" jstcache="30">null</a>
									</p>
								</div>
							</div>
						</div>
					</div>
					<div id="diagnose-frame" class="hidden" jstcache="0"></div>
					<div id="download-links-wrapper" class="hidden" jstcache="0">
						<div id="download-link-wrapper" jstcache="0">
							<a id="download-link" class="link-button" onclick="downloadButtonClick()" jsselect="downloadButton" jscontent="msg" jsvalues=".disabledText:disabledMsg" jstcache="12" style="display: none;">
							</a>
						</div>
						<div id="download-link-clicked-wrapper" class="hidden" jstcache="0">
							<div id="download-link-clicked" class="link-button" jsselect="downloadButton" jscontent="disabledMsg" jstcache="23" style="display: none;">
							</div>
						</div>
					</div>
					<div id="offline-content-list" hidden="" jstcache="0">
						<div class="offline-content-list-title" jsselect="offlineContentList" jscontent="title" jstcache="16" style="display: none;"></div>
						<div id="offline-content-suggestions" jstcache="0"></div>
						<div class="offline-content-list-action" jstcache="0">
							<a class="link-button" onclick="launchDownloadsPage()" jsselect="offlineContentList" jscontent="actionText" jstcache="24" style="display: none;">
							</a>
						</div>
					</div>
					<div id="offline-content-summary" onclick="launchDownloadsPage()" hidden="" jstcache="0">
						<div class="offline-content-summary-images" jstcache="0">
							<div class="offline-content-summary-image-truncate" jstcache="0">
								<img id="earth" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMmM1LjUyIDAgMTAgNC40OCAxMCAxMHMtNC40OCAxMC0xMCAxMFMyIDE3LjUyIDIgMTIgNi40OCAyIDEyIDJ6TTQgMTJoNC40YzMuNDA3LjAyMiA0LjkyMiAxLjczIDQuNTQzIDUuMTI3SDkuNDg4djIuNDdhOC4wMDQgOC4wMDQgMCAwIDAgMTAuNDk4LTguMDgzQzE5LjMyNyAxMi41MDQgMTguMzMyIDEzIDE3IDEzYy0yLjEzNyAwLTMuMjA2LS45MTYtMy4yMDYtMi43NWgtMy43NDhjLS4yNzQtMi43MjguNjgzLTQuMDkyIDIuODctNC4wOTIgMC0uOTc1LjMyNy0xLjU5Ny44MTEtMS45N0E4LjAwNCA4LjAwNCAwIDAgMCA0IDEyeiIgZmlsbD0iIzNDNDA0MyIvPjwvc3ZnPg==" jstcache="0">
							</div>
							<div class="offline-content-summary-image-truncate" jstcache="0">
								<img id="music-note" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTIgM3Y5LjI2Yy0uNS0uMTctMS0uMjYtMS41LS4yNkM4IDEyIDYgMTQgNiAxNi41UzggMjEgMTAuNSAyMXM0LjUtMiA0LjUtNC41VjZoNFYzaC03eiIgZmlsbD0iIzNDNDA0MyIvPjwvc3ZnPg==" jstcache="0">
							</div>
							<div class="offline-content-summary-image-truncate" jstcache="0">
								<img id="video" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTcgMTAuNVY3YTEgMSAwIDAgMC0xLTFINGExIDEgMCAwIDAtMSAxdjEwYTEgMSAwIDAgMCAxIDFoMTJhMSAxIDAgMCAwIDEtMXYtMy41bDQgNHYtMTFsLTQgNHoiIGZpbGw9IiMzQzQwNDMiLz48L3N2Zz4=" jstcache="0">
							</div>
							<div jstcache="0">
								<!-- Pump Follow Up Bug #20954431 -->
							</div>
						</div>
						<div class="offline-content-summary-description" jsselect="offlineContentSummary" jscontent="description" jstcache="17" style="display: none;">
						</div>
						<a class="offline-content-summary-action link-button" jsselect="offlineContentSummary" jscontent="actionText" jstcache="18" style="display: none;">
						</a>
					</div>
				</div>
			</div>
			<div id="buttons" class="nav-wrapper suggested-left" jstcache="0">
				<div id="control-buttons" jstcache="0">
					<button id="show-saved-copy-button" class="blue-button text-button" onclick="showSavedCopyButtonClick()" jsselect="showSavedCopyButton" jscontent="msg" jsvalues="title:title; .primary:primary" jstcache="11" style="display: none;">
					</button>
					<button id="reload-button" class="blue-button text-button" onclick="reloadButtonClick(this.url);" jsselect="reloadButton" jsvalues=".url:reloadUrl" jscontent="msg" jstcache="9">刷新</button>
					<button id="diagnose-button" class="blue-button text-button" onclick="diagnoseErrors()" jsselect="diagnoseButton" jscontent="msg" jstcache="10" style="display: none;">
					</button>

					<button id="download-button" class="blue-button text-button" onclick="downloadButtonClick()" jsselect="downloadButton" jscontent="msg" jsvalues=".disabledText:disabledMsg" jstcache="12" style="display: none;">
					</button>
					<button id="secondary-reload-button" class="blue-button text-button hidden" onclick="reloadButtonClick(this.url);" jsselect="reloadButton" jsvalues=".url:reloadUrl" jscontent="msg" jstcache="9">刷新</button>
				</div>
				<div id="game-div" jsdisplay="!!showGameButtons" jstcache="5" style="display: none;">
					<div class="game-split-line" jstcache="0"></div>
					<div id="game-buttons" jstcache="0">
						<span id="game-message" jscontent="playGameMsg" jstcache="19"></span>
						<div class="managed-icon" jsdisplay="!!disabledGame" jstcache="20"></div>
						<button id="game-button" jsselect="gameButton" onclick="launchGame()" jstcache="21">
							<div class="icon-play-game-button" alt="" jstcache="0"></div>
							<div class="game-button-msg" jscontent="msg" jstcache="25">
							</div>
						</button>
					</div>
				</div>
			</div>
		</div>
		<div class="footer" jstcache="0">
			<div class="left-footer" jstcache="0">
				<div class="edge-logo" alt="" jstcache="0"></div>
				<div class="edge-branding-text" jsselect="footer" jsvalues=".innerHTML:msg" jstcache="6">Microsoft Edge</div>
			</div>
		</div>
		<div id="sub-frame-error" jstcache="0">
			<!-- Show details when hovering over the icon, in case the details are
           hidden because they're too large. -->
			<div class="icon icon-elixir-thinking" jseval="updateIconClass(this.classList, iconClass)" jstcache="1"></div>
			<div id="sub-frame-error-details" jsselect="summary" jsvalues=".innerHTML:msg" jstcache="2">
				<strong jscontent="hostName" jstcache="32">127.0.0.1</strong> 已拒绝连接。
			</div>
		</div>

		<!-- [China 1B] Add search box and Topsites to the page if feature flag is true and the network error is not an offline error -->
		<div class="bing-search hidden" id="neterror-bing-search" jstcache="0">
			<!-- Search box -->
			<div class="search-input" jsdisplay="edge_vnext.showSearchBox" jstcache="3" style="display: none;">
				<input id="bing-input" type="text" jsvalues=".placeholder:edge_vnext.searchBoxHint" onkeydown="handleKeyDown(event);" jstcache="7">
				<button class="search-icon" onclick="bingSearchClick();" jstcache="0">
					<svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 25 24" fill="none" jstcache="0">
						<path d="M10.6699 2.75C14.674 2.75 17.9199 5.99594 17.9199 10C17.9199 11.7319 17.3127 13.3219 16.2995 14.5688L21.2003 19.4697C21.4931 19.7626 21.4931 20.2374 21.2003 20.5303C20.934 20.7966 20.5173 20.8208 20.2237 20.6029L20.1396 20.5303L15.2387 15.6295C13.9918 16.6427 12.4018 17.25 10.6699 17.25C6.66586 17.25 3.41992 14.0041 3.41992 10C3.41992 5.99594 6.66586 2.75 10.6699 2.75ZM10.6699 4.25C7.49428 4.25 4.91992 6.82436 4.91992 10C4.91992 13.1756 7.49428 15.75 10.6699 15.75C13.8456 15.75 16.4199 13.1756 16.4199 10C16.4199 6.82436 13.8456 4.25 10.6699 4.25Z" fill="white" jstcache="0"></path>
					</svg>
				</button>
			</div>

			<!-- Topsites -->
			<div class="top-sites" jsdisplay="(edge_vnext.showTopsites &amp;&amp; topSites &amp;&amp; topSites.length)" jstcache="4" style="display: none;">
				<div class="site-item" tabindex="0" jsselect="topSites" jsvalues=".url:url" onclick="handleTopSiteClick(this.url);" onkeydown="handleTopSiteKeydown(event,this.url)" jstcache="8">
					<div class="site-image" jstcache="0">
						<img jsvalues=".src:faviconUrl" jstcache="22">
					</div>
					<div class="title" jscontent="title" jstcache="13"></div>
				</div>
			</div>
		</div>



		<script jstcache="0">
			var loadTimeDataRaw = {"details":"详细信息","errorCode":"ERR_CONNECTION_REFUSED","fontfamily":"'Segoe UI',Arial,'Microsoft Yahei',sans-serif","fontfamilyMd":"'Segoe UI',Arial,'Microsoft Yahei',sans-serif","fontsize":"75%","footer":{"msg":"Microsoft Edge"},"heading":{"hostName":"127.0.0.1","msg":"嗯… 无法访问此页面"},"hideDetails":"隐藏详细信息","iconClass":"icon-elixir-thinking","is_windows_xbox_sku":"false","language":"zh","reloadButton":{"msg":"刷新","reloadUrl":"http://127.0.0.1:5/"},"suggestionsDetails":[{"body":"请检查你的网络电缆、调制解调器和路由器。","header":"检查 Internet 连接"},{"body":"如果它已被列为允许访问网络的程序，请尝试\n将其从列表中删除，然后重新添加。","header":"要允许 Microsoft Edge 访问网络，请在防火墙或防病毒软件中进行\n          设置。"},{"advancedTitle":"显示高级设置","body":"请检查代理设置。你可能需要向组织询问代理服务器是否正在工作。如果你认为不应该使用代理服务器，请转到\n          “Microsoft Edge”菜单 >\n          \u003Cspan jscontent=\"settingsTitle\">\u003C/span>\n          >\n          \u003Cspan jscontent=\"advancedTitle\">\u003C/span>\n          >\n          \u003Cspan jscontent=\"proxyTitle\">\u003C/span>\n          >\n          LAN 设置\n          并取消选中“为 LAN 使用代理服务器”复选框。","header":"如果使用代理服务器:","privacySecurityTitle":"隐私和安全","proxyTitle":"打开计算机的代理设置","settingsTitle":"设置","systemTitle":"系统"}],"suggestionsSummaryList":[{"clickData":"0","searchTerms":"127 0 0 1","searchUrl":"https://www.bing.com/search?form=ANLKDR&q=127 0 0 1","summary":"在 web 上搜索 \u003Ca jsvalues=\"href:searchUrl;.jstdata:$this\" onclick=\"navigationCorrectionClicked(this.jstdata)\" jscontent=\"searchTerms\" id=\"search-link\">\u003C/a>"},{"summary":"检查连接"},{"summary":"\u003Ca href=\"#buttons\" onclick=\"toggleHelpBox()\">检查代理和防火墙\u003C/a>"}],"suggestionsSummaryListHeader":"请尝试：","summary":{"failedUrl":"http://127.0.0.1:5/","hostName":"127.0.0.1","msg":"\u003Cstrong jscontent=\"hostName\">\u003C/strong> 已拒绝连接。"},"textdirection":"ltr","title":"127.0.0.1"};
		</script>
	</body>
</html>"""