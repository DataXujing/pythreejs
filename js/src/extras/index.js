//
// This file auto-generated with generate-wrappers.js
// Date: Thu Oct 20 2016 12:05:53 GMT-0700 (PDT)
//
// Load all three.js python wrappers
var loadedModules = [
    require('./CurveUtils.autogen.js'),
    require('./SceneUtils.autogen.js'),
    require('./ShapeUtils.autogen.js'),
    require('./core'),
    require('./curves'),
    require('./geometries'),
    require('./helpers'),
    require('./objects'),
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

