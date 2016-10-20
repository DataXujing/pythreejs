//
// This file auto-generated with generate-wrappers.js
// Date: Thu Oct 20 2016 12:05:53 GMT-0700 (PDT)
//
// Load all three.js python wrappers
var loadedModules = [
    require('./MomentumCameraControls.js'),
    require('./OrbitControls.js'),
    require('./TrackballControls.js'),
];

for (var i in loadedModules) {
    if (loadedModules.hasOwnProperty(i)) {
        var loadedModule = loadedModules[i];
        for (var target_name in loadedModule) {
            if (loadedModule.hasOwnProperty(target_name)) {
                module.exports[target_name] = loadedModule[target_name];
            }
        }
    }
}

