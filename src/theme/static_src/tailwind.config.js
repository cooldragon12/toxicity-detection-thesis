/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
const plugin = require('tailwindcss/plugin')
module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        screens: {
            sm: '480px',
            md: '768px',
            lg: '976px',
            xl: '1440px',
          },
        extend: {
            colors: {
                  primary: '#FD4556',
                  secondary: '#BD3944',
                  text:'#000000',
                  accent: '#53212B',
                  background_cc:'#FFFBF5'
              },
            
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        plugin(function({ addComponents }) {
            addComponents({
                '.input_container': {
                    position: 'relative',
                    marginBottom: '1.5rem',
                    width: '80%',
                    borderRadius: '0.5rem',
                    
                    '& > input[type=text], > input[type=email], > input[type=number] ':{
                        border: 'none',
                        borderBottom: '0.122em solid #BD3944',
                        height: '2rem',
                        width: '100%',
                        fontSize: '1.0625rem',
                        paddingLeft: '0.6rem',
                        lineHeight: '147.6%',
                        paddingTop: '0.825rem',
                        paddingBottom: '0.5rem',
                        transition: 'all 0.3s ease-in-out',
                        
                    },
                    '& label':{
                        position: 'absolute',
                        transform: 'translateY(-0.7rem)',
                        // transform: 'translateY(0.5rem)',
                        fontSize: '1rem',
                        color: 'grey',
                        padding: '0 0.25rem',
                        transition: 'all 0.3s ease-in-out',
                        userSelect: 'none',
                        cursor: 'text',
                        
                    },
                    '&:focus-within label':{
                        transform: 'translateY(-0.7rem)',
                        fontSize: '0.8rem',
                        color: '#FD4556',
                        padding: '0 0.25rem',
                        backgroundColor: '#ffff',
                    },
                    
                },
                

            })
        })
    ],
}
