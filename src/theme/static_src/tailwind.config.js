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
                    margin: '0.5rem',
                    width: '100%',
                    
                    '& input, & select':{
                        width: '100%',
                        border: '2px solid #ccc',
                        padding: '0.5rem',
                        transition: 'all 0.3s ease-in-out',
                        borderRadius: '0.5rem',
                        outline: 'none',
                        fontSize: '1em',
                        '&:focus, &:valid':{
                            boxShadow: 'none',
                            borderColor: '#FD4556',
                            '+ .input-text-label':{
                                transform: 'translate(0.5rem,-1rem)',
                                fontSize: '0.8rem',
                                color: '#FD4556',
                                padding: '0 0.25rem',
                                backgroundColor: '#ffff',
                                letterSpacing: '0.1rem',
                                padding: '0 0.5rem',
                                borderRight: '0.122em solid #BD3944',
                                borderLeft: '0.122em solid #BD3944',
                            }
                        }
                    },
                    '& input[type=radio]':{
                        color: '#BD3944',
                        borderRadius: '100%',
                        width: '1rem',
                        '&:hover':{
                            cursor: 'pointer',
                            borderColor: '#FD4556',
                        }
                    },
                    '& .input-text-label':{
                        position: 'absolute',
                        // transform: 'translateY(-0.7rem)',
                        top: '0.5rem',
                        left: '0.5rem',
                        fontSize: '1rem',
                        color: 'gray',
                        padding: '0 0.25rem',
                        transition: 'all 0.3s ease-in-out',
                        userSelect: 'none',
                        cursor: 'text',
                        border: 'none',
                    },

                    // '&:focus,&:valid': {
                    //     borderColor: '#FD4556',
                    //     '.input-text-label':{
                    //     transform: 'translate(0.5rem,-0.7rem)',
                    //     fontSize: '0.8rem',
                    //     color: '#FD4556',
                    //     padding: '0 0.25rem',
                    //     backgroundColor: '#ffff',
                    //     letterSpacing: '0.1rem',
                    //     padding: '0 0.5rem',
                    //     borderRight: '0.122em solid #BD3944',
                    //     borderLeft: '0.122em solid #BD3944',
                    // }},
                    
                },
                '.input_container_dropdown': {
                    position: 'relative',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    margin: '0.5rem',

                    // width: '100%',
                    borderRadius: '0.5rem',
                    border: '2px dashed #ccc',
                    width: '300px',
                    height: '200px',
                    margin: '0 auto',
                    textAlign: 'center',
                    fontSize: '18px',
                    transition: 'all 0.3s ease-in-out',
                    '& .drop-zone-label':{
                        fontWeight: 'bold',
                        color: '#999',
                        userSelect: 'none',
                        
                    },
                    '& input':{
                        display: 'none'
                    },
                    '&:hover':{
                        cursor: 'pointer',
                        borderColor: '#666'
                    },
                    '&:hover .drop-zone-label':{
                        color: '#666',
                        cursor: 'pointer',

                    },
                    '&.drop-zone-active':{
                        borderColor: '#FD4556',
                        backgroundColor: '#ffff',
                        
                    },
                    '& drop-zone-preview':{
                        position: 'absolute',
                        top: '0',
                        left: '0',
                        width: '100%',
                        height: '100%',
                        objectFit: 'cover',
                        borderRadius: '0.5rem',
                        border: '2px dashed #ccc',
                        '& .drop-zone__image-preview': {
                            maxWidth: '100%',
                            maxHeight: '100%',
                          },
                        
                        '& .drop-zone__image-preview img': {
                            maxWidth: '100%',
                            maxHeight: '100%',
                          }
                        
                    },
                },
                '.form_visible':{
                    left: '0%',
                    opacity: '1',
                },
                '.form_hidden':{
                    left: '-100%',
                    opacity: '0',
                },

            })
        })
    ],
}
